"""
Aegis V0 — Verification pipeline (stubs only)

Verifiers examine a dry-run Plan and produce explain-only findings.
They do not execute actions, mutate state, or approve execution.

Authoritative constraints:
- AEGIS_IMPLEMENTATION_ROADMAP.md (V0 — Skeleton)
- AEGIS_SECURITY_MODEL.md
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from orchestrator.plan import Plan, PlanStep


class VerificationLevel(str, Enum):
    PASS = "pass"
    WARN = "warn"
    BLOCK = "block"


@dataclass(frozen=True)
class VerificationFinding:
    level: VerificationLevel
    message: str
    step_id: Optional[int] = None


@dataclass(frozen=True)
class VerificationReport:
    findings: List[VerificationFinding]

    @property
    def has_blockers(self) -> bool:
        return any(f.level == VerificationLevel.BLOCK for f in self.findings)

    def to_dict(self):
        return {
            "findings": [
                {
                    "level": f.level.value,
                    "message": f.message,
                    "step_id": f.step_id,
                }
                for f in self.findings
            ]
        }


# ---- Verifier stubs ----

def verify_requires_confirmation(plan: Plan) -> List[VerificationFinding]:
    """
    Warn if a step with Medium or High risk does not require confirmation.
    """
    findings: List[VerificationFinding] = []

    for step in plan.steps:
        if step.risk.value in ("Medium", "High") and not step.requires_confirmation:
            findings.append(
                VerificationFinding(
                    level=VerificationLevel.WARN,
                    step_id=step.step_id,
                    message=(
                        f"Step {step.step_id} has risk level '{step.risk.value}' "
                        "but does not require explicit confirmation."
                    ),
                )
            )

    return findings


def verify_scope_is_present(plan: Plan) -> List[VerificationFinding]:
    """
    Block if any step lacks scope constraints entirely.
    """
    findings: List[VerificationFinding] = []

    for step in plan.steps:
        constraints = step.scope.constraints
        if not any(
            [
                constraints.paths,
                constraints.domains,
                constraints.apps,
                constraints.methods,
                constraints.max_bytes is not None,
            ]
        ):
            findings.append(
                VerificationFinding(
                    level=VerificationLevel.BLOCK,
                    step_id=step.step_id,
                    message=(
                        f"Step {step.step_id} has no scope constraints defined. "
                        "Unbounded scope is not permitted."
                    ),
                )
            )

    return findings


# ---- Verification entry point ----

def run_verification(plan: Plan) -> VerificationReport:
    """
    Run all V0 verifier stubs against a plan and return a report.
    """
    findings: List[VerificationFinding] = []

    findings.extend(verify_requires_confirmation(plan))
    findings.extend(verify_scope_is_present(plan))

    return VerificationReport(findings=findings)
