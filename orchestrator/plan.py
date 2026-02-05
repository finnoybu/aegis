"""
Plan representation for Aegis (Phase 1).

A Plan is a hypothetical, dry-run description of steps that *would* be taken
to satisfy an Intent. It has no execution authority and performs no actions.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List, Optional
import uuid


@dataclass(frozen=True)
class PlanStep:
    """
    A single hypothetical step in a plan.

    Describes *what would be done*, not how to do it.
    """
    step_id: str
    description: str
    required_capability: str  # e.g. "filesystem.modify", "packages.install"
    estimated_risk: str       # coarse label: "low", "medium", "high"
    notes: Optional[str] = None


@dataclass(frozen=True)
class PlanMetadata:
    """
    Contextual metadata about the plan.
    """
    plan_id: str
    created_at: datetime
    intent_request_id: str


@dataclass(frozen=True)
class Plan:
    """
    Canonical dry-run plan derived from an Intent.

    This structure is immutable and side-effect free.
    """
    steps: List[PlanStep]
    summary: str
    metadata: PlanMetadata


def create_plan(
    *,
    intent_request_id: str,
    steps: List[PlanStep],
    summary: str,
) -> Plan:
    """
    Factory function to create a Plan safely.
    """
    metadata = PlanMetadata(
        plan_id=str(uuid.uuid4()),
        created_at=datetime.now(timezone.utc),
        intent_request_id=intent_request_id,
    )

    return Plan(
        steps=steps,
        summary=summary,
        metadata=metadata,
    )
