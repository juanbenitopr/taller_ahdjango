from dataclasses import dataclass


@dataclass(frozen=True)
class RetrieveAccountCommand:
    account_id: int
