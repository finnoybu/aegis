"""
Aegis V0 — Mediation Orchestrator (Non-Executing)

This module wires together the mediation pipeline:

Intent
  → Dry-run Plan
    → Verification
      → Refusal Decision

It performs no execution, no approval handling, and no persistence.
All logic here is compositional and deterministic.

Authoritative behavior:
- AEGIS_IMPLEMENTATION_ROADMAP.md (V0 — Skeleton)
- AEGIS_INTENT_CARD_SPEC.md
- AEGIS_REFUSAL_GUIDELINES.md
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

from orchestrator.intent import Intent
from orchestrator.plan import create_dry_run_plan, Plan
from orchestrator.verification import verify_plan, VerificationResult
from orchestrator.refusal import decide_refusal, RefusalDecision


@dataclass(frozen=True)
class MediationResult:
    """
    Canon-adjacent aggregation of mediation outcomes.

    This object is NOT part of a canonical schema yet.
    It exists to allow inspection, debugging, and future UI rendering.
    """
    intent: Intent
    plan: Optional[Plan]
    verification: Optional[VerificationResult]
    refusal: Optional[RefusalDecision]


def mediate_intent(
    *,
    intent: Intent,
    allowed_actions_json: Dict[str, Any],
) -> MediationResult:
    """
    Perform full mediation for a single intent.

    Steps:
    1. Generate dry-run plan
    2. Verify plan against policy and constraints
    3. Decide refusal / clarification / proceed state

    No execution or approval logic exists here.
    """

    # ---- Step 1: Plan generation (dry-run only) ----
    try:
        plan, _audit = create_dry_run_plan(
            derived_from_intent_id=intent.intent_id,
            requested_steps=intent.requested_steps,
            allowed_actions_json=allowed_actions_json,
            notes="Generated via V0 mediation pipeline",
        )
    except Exception as e:
        # Planning failure is treated as a refusal condition
        refusal = decide_refusal(
            intent=intent,
            plan=None,
            verification=None,
            error=str(e),
        )
        return MediationResult(
            intent=intent,
            plan=None,
            verification=None,
            refusal=refusal,
        )

    # ---- Step 2: Verification ----
    verification = verify_plan(plan)

    # ---- Step 3: Refusal / clarification decision ----
    refusal = decide_refusal(
        intent=intent,
        plan=plan,
        verification=verification,
        error=None,
    )

    return MediationResult(
        intent=intent,
        plan=plan,
        verification=verification,
        refusal=refusal,
    )
