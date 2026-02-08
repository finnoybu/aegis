"""
Aegis V0 — Dry-run planning (plan generation only)

This module produces a *non-executable* Plan from already-understood intent.
It performs no system actions and has no side effects.

Authoritative structure: AEGIS_ACTION_SCHEMA.json ($defs.plan, $defs.planStep)
Allowed actions/risk/reversibility: AEGIS_ALLOWED_ACTIONS_V1.json
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple
import uuid


class RiskLevel(str, Enum):
    # Must match AEGIS_ACTION_SCHEMA.json enum exactly
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


@dataclass(frozen=True)
class ScopeConstraints:
    # Mirrors $defs.scopeSpec.properties.constraints
    paths: List[str] = field(default_factory=list)
    domains: List[str] = field(default_factory=list)
    apps: List[str] = field(default_factory=list)
    methods: List[str] = field(default_factory=list)
    max_bytes: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {
            "paths": list(self.paths),
            "domains": list(self.domains),
            "apps": list(self.apps),
            "methods": list(self.methods),
        }
        if self.max_bytes is not None:
            d["max_bytes"] = int(self.max_bytes)
        return d


@dataclass(frozen=True)
class ScopeSpec:
    # Mirrors $defs.scopeSpec
    scope_token: str
    constraints: ScopeConstraints = field(default_factory=ScopeConstraints)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "scope_token": self.scope_token,
            "constraints": self.constraints.to_dict(),
        }


@dataclass(frozen=True)
class PlanStep:
    # Mirrors $defs.planStep
    step_id: int                     # schema: integer >= 1
    action: str                      # must exist in AEGIS_ALLOWED_ACTIONS_V1.json
    args: Dict[str, Any]             # schema: object
    scope: ScopeSpec                 # schema: scopeSpec
    risk: RiskLevel                  # schema: riskLevel enum
    reversible: bool
    requires_confirmation: bool
    validators: List[str] = field(default_factory=list)
    dry_run_supported: bool = True

    def to_dict(self) -> Dict[str, Any]:
        return {
            "step_id": int(self.step_id),
            "action": self.action,
            "args": dict(self.args),
            "scope": self.scope.to_dict(),
            "risk": self.risk.value,
            "reversible": bool(self.reversible),
            "requires_confirmation": bool(self.requires_confirmation),
            "validators": list(self.validators),
            "dry_run_supported": bool(self.dry_run_supported),
        }


@dataclass(frozen=True)
class Plan:
    # Mirrors $defs.plan
    plan_id: str
    steps: List[PlanStep]
    notes: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {
            "plan_id": self.plan_id,
            "steps": [s.to_dict() for s in self.steps],
        }
        if self.notes:
            d["notes"] = self.notes
        return d


@dataclass(frozen=True)
class PlanAudit:
    """
    Lightweight, in-memory-only metadata for debugging and traceability.
    Not part of the canonical schema. Do not persist in V0 unless documented.
    """
    created_at: datetime
    derived_from_intent_id: str


# ---- Allowed actions registry helpers ----

def build_allowed_action_index(allowed_actions_json: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """
    Build a fast lookup: action -> policy entry.

    expected shape:
      { "allowed_actions": [ { "action": "...", "risk": "Low|Medium|High", "reversible": bool, ... }, ... ] }
    """
    entries = allowed_actions_json.get("allowed_actions", [])
    index: Dict[str, Dict[str, Any]] = {}
    for entry in entries:
        action = entry.get("action")
        if isinstance(action, str) and action:
            index[action] = entry
    return index


def _coerce_risk(risk_str: str) -> RiskLevel:
    try:
        return RiskLevel(risk_str)
    except Exception as e:
        raise ValueError(f"Invalid risk level '{risk_str}'. Must be one of: {[r.value for r in RiskLevel]}") from e


# ---- Validation ----

def validate_step_schema(step: PlanStep) -> List[str]:
    """
    Minimal structural validation consistent with AEGIS_ACTION_SCHEMA.json.
    We avoid pulling in a full jsonschema dependency in V0.
    """
    errors: List[str] = []

    if step.step_id < 1:
        errors.append("step_id must be >= 1.")

    if not isinstance(step.action, str) or not step.action.strip():
        errors.append("action must be a non-empty string.")

    if not isinstance(step.args, dict):
        errors.append("args must be an object (dict).")

    if not isinstance(step.scope.scope_token, str) or not step.scope.scope_token.strip():
        errors.append("scope.scope_token must be a non-empty string.")

    # constraints additionalProperties=False: we ensure only known fields exist via dataclass
    if step.scope.constraints.max_bytes is not None and step.scope.constraints.max_bytes < 0:
        errors.append("scope.constraints.max_bytes must be >= 0 when provided.")

    # risk must be RiskLevel enum
    if not isinstance(step.risk, RiskLevel):
        errors.append("risk must be one of: Low, Medium, High.")

    if not isinstance(step.reversible, bool):
        errors.append("reversible must be boolean.")

    if not isinstance(step.requires_confirmation, bool):
        errors.append("requires_confirmation must be boolean.")

    if not isinstance(step.validators, list) or any(not isinstance(v, str) for v in step.validators):
        errors.append("validators must be a list of strings.")

    if not isinstance(step.dry_run_supported, bool):
        errors.append("dry_run_supported must be boolean.")

    return errors


def validate_plan(plan: Plan, allowed_action_index: Dict[str, Dict[str, Any]]) -> List[str]:
    errors: List[str] = []

    if not isinstance(plan.plan_id, str) or not plan.plan_id.strip():
        errors.append("plan_id must be a non-empty string.")

    if not plan.steps:
        errors.append("steps must contain at least one step.")

    # step ids must be unique and start at 1 (recommended)
    step_ids = [s.step_id for s in plan.steps]
    if len(step_ids) != len(set(step_ids)):
        errors.append("step_id values must be unique within a plan.")
    if step_ids and min(step_ids) < 1:
        errors.append("step_id values must be >= 1.")

    # action must be allowed
    for s in plan.steps:
        if s.action not in allowed_action_index:
            errors.append(f"Step {s.step_id}: action '{s.action}' is not present in AEGIS_ALLOWED_ACTIONS_V1.json.")

    # structural step validation
    for s in plan.steps:
        for err in validate_step_schema(s):
            errors.append(f"Step {s.step_id}: {err}")

    return errors


# ---- Plan construction ----

def create_dry_run_plan(
    *,
    derived_from_intent_id: str,
    requested_steps: List[Dict[str, Any]],
    allowed_actions_json: Dict[str, Any],
    notes: Optional[str] = None,
) -> Tuple[Plan, PlanAudit]:
    """
    Create a Plan from requested step descriptions.

    requested_steps items are dicts with:
      - action: str
      - args: dict (optional; default {})
      - scope_token: str
      - constraints: dict (optional; may include paths/domains/apps/methods/max_bytes)
      - requires_confirmation: bool (optional; default True)
      - validators: list[str] (optional; default [])
      - dry_run_supported: bool (optional; default True)

    risk/reversible are derived from AEGIS_ALLOWED_ACTIONS_V1.json for the action.
    """
    allowed_index = build_allowed_action_index(allowed_actions_json)

    steps: List[PlanStep] = []
    for i, raw in enumerate(requested_steps, start=1):
        action = raw.get("action")
        if not isinstance(action, str) or not action.strip():
            raise ValueError(f"Step {i}: missing/invalid 'action'.")

        policy = allowed_index.get(action)
        if policy is None:
            raise ValueError(f"Step {i}: action '{action}' is not allowed by AEGIS_ALLOWED_ACTIONS_V1.json.")

        risk = _coerce_risk(str(policy.get("risk")))
        reversible = bool(policy.get("reversible", False))

        scope_token = raw.get("scope_token")
        if not isinstance(scope_token, str) or not scope_token.strip():
            raise ValueError(f"Step {i}: missing/invalid 'scope_token'.")

        constraints_raw = raw.get("constraints", {}) or {}
        if not isinstance(constraints_raw, dict):
            raise ValueError(f"Step {i}: 'constraints' must be an object when provided.")

        constraints = ScopeConstraints(
            paths=list(constraints_raw.get("paths", []) or []),
            domains=list(constraints_raw.get("domains", []) or []),
            apps=list(constraints_raw.get("apps", []) or []),
            methods=list(constraints_raw.get("methods", []) or []),
            max_bytes=constraints_raw.get("max_bytes", None),
        )

        step = PlanStep(
            step_id=i,
            action=action,
            args=dict(raw.get("args", {}) or {}),
            scope=ScopeSpec(scope_token=scope_token, constraints=constraints),
            risk=risk,
            reversible=reversible,
            requires_confirmation=bool(raw.get("requires_confirmation", True)),
            validators=list(raw.get("validators", []) or []),
            dry_run_supported=bool(raw.get("dry_run_supported", True)),
        )
        steps.append(step)

    plan = Plan(plan_id=str(uuid.uuid4()), steps=steps, notes=notes)
    audit = PlanAudit(created_at=datetime.now(timezone.utc), derived_from_intent_id=derived_from_intent_id)

    # final validation (defensive)
    errors = validate_plan(plan, build_allowed_action_index(allowed_actions_json))
    if errors:
        raise ValueError("Plan failed validation:\n- " + "\n- ".join(errors))

    return plan, audit
