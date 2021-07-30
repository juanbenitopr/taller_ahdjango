from dataclasses import dataclass


@dataclass(frozen=True)
class ListAccountCommand:
    owner_id: int
