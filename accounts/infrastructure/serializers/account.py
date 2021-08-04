from pydantic import BaseModel


class AccountSerializer(BaseModel):
    owner_id: int
    amount: float

    class Config:
        orm_mode = True
