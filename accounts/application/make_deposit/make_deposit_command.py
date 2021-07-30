from dataclasses import dataclass


@dataclass(frozen=True)
class MakeDepositCommand:
    account_id: int
    amount: float
