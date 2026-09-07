from dataclasses import dataclass


@dataclass(frozen=True)
class Alert:
    title: str
    description: str
    score: int
    entity_type: str
    entity_id: str
