from dataclasses import dataclass


@dataclass
class Account:
    id: int
    amount: float
    owner_id: int

    def deposit(self, amount: float) -> float:
        self.amount += amount

        return self.amount
