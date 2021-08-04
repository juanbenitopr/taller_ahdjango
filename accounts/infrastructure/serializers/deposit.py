from pydantic import BaseModel


class DepositSerializer(BaseModel):
    account_id: int
    amount: float
