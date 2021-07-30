import abc
from typing import List

from accounts.domain.account import Account


class AccountRepository(abc.ABC):

    @abc.abstractmethod
    def get_by_id(self, id: int) -> Account:
        pass

    @abc.abstractmethod
    def get_all_by_user_id(self, user_id: int) -> List[Account]:
        pass

    @abc.abstractmethod
    def save(self, account: Account) -> List[Account]:
        pass
