"""
Aegis V0 — Refusal & Decision Logic (No Execution)

This module determines whether Aegis should:
- Proceed (PASS)
- Proceed with warnings (WARN)
- Refuse (REFUSE)

It performs no actions, approvals, or side effects.

Authoritative sources:
- AEGIS_REFUSAL_GUIDELINES.md
- AEGIS_IMPLEMENTATION_ROADMAP.md (V0 — Refusal behavior)
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List

from orchestrator.intent import Intent
from orchestrator.plan import Plan
from orchestrator.verification import VerificationReport, VerificationSeverity


class RefusalDecisionType(str, Enum):
    PASS = "PASS"
    WARN = "WARN"
    REFUSE = "REFUSE"


@dataclass(frozen=True)
class RefusalReason:
    severity: VerificationSeverity
    code: str
    message: str
    step_id: int | None = None


@dataclass(frozen=True)
class RefusalDecision:
    """
    Canonical refusal decision object.

    This object is informational only.
    It does not trigger execution, approval, or UI behavior.
    """
    decision: RefusalDecisionType
    reasons: List[RefusalReason]
    summary: str


# ---- Decision Logic ----

def decide_refusal(
    *,
    intent: Intent,
    plan: Plan,
    verification: VerificationReport,
) -> RefusalDecision:
    """
    Determine whether the plan may proceed, must warn, or must refuse.

    Rules (V0):
    - Any BLOCK finding → REFUSE
    - WARN findings only → WARN
    - PASS only → PASS
    """

    reasons: List[RefusalReason] = []

    has_block = False
    has_warn = False

    for finding in verification.findings:
        reason = RefusalReason(
            severity=finding.severity,
            code=finding.code,
            message=finding.message,
            step_id=finding.step_id,
        )
        reasons.append(reason)

        if finding.severity == VerificationSeverity.BLOCK:
            has_block = True
        elif finding.severity == VerificationSeverity.WARN:
            has_warn = True

    if has_block:
        return RefusalDecision(
            decision=RefusalDecisionType.REFUSE,
            reasons=reasons,
            summary="Plan refused due to blocking verification findings.",
        )

    if has_warn:
        return RefusalDecision(
            decision=RefusalDecisionType.WARN,
            reasons=reasons,
            summary="Plan may proceed with warnings requiring human review.",
        )

    return RefusalDecision(
        decision=RefusalDecisionType.PASS,
        reasons=reasons,
        summary="Plan passed verification with no blocking findings.",
    )
