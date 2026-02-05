"""
Intent representation for Aegis (Phase 1).

An Intent is a record of human intent.
It is not a command.
It has no execution authority.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List, Optional, Dict
import uuid


@dataclass(frozen=True)
class IntentMetadata:
    """
    Contextual metadata about the intent request.
    """
    request_id: str
    timestamp: datetime
    source: str  # e.g. "cli", "api", "web"
    user_id: Optional[str] = None


@dataclass(frozen=True)
class Intent:
    """
    Canonical representation of human intent.

    This structure is immutable and side-effect free.
    """
    raw_input: str
    goal: str
    scope: List[str]
    constraints: Dict[str, str] = field(default_factory=dict)
    assumptions: Dict[str, str] = field(default_factory=dict)
    metadata: IntentMetadata = field(default_factory=lambda: IntentMetadata(
        request_id=str(uuid.uuid4()),
        timestamp=datetime.now(timezone.utc),
        source="unknown",
    ))


def create_intent(
    raw_input: str,
    goal: str,
    scope: List[str],
    *,
    constraints: Optional[Dict[str, str]] = None,
    assumptions: Optional[Dict[str, str]] = None,
    source: str = "cli",
    user_id: Optional[str] = None,
) -> Intent:
    """
    Factory function to create an Intent safely.
    """
    metadata = IntentMetadata(
        request_id=str(uuid.uuid4()),
        timestamp=datetime.now(timezone.utc),
        source=source,
        user_id=user_id,
    )

    return Intent(
        raw_input=raw_input,
        goal=goal,
        scope=scope,
        constraints=constraints or {},
        assumptions=assumptions or {},
        metadata=metadata,
    )
