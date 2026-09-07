from dataclasses import dataclass


@dataclass(frozen=True)
class RuleResult:
    name: str
    triggered: bool
    contribution: float
    explanation: str


def high_amount(amount: float, limit: float) -> RuleResult:
    triggered = amount > limit
    return RuleResult("high_amount", triggered, 80 if triggered else 0, f"Amount {amount} exceeds limit {limit}")
