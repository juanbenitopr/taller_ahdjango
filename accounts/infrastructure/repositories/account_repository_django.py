from typing import List, Optional

from django.db import IntegrityError

from accounts.domain.account import Account as AccountDomain
from accounts.domain.repositories.account_repository import AccountRepository
from accounts.infrastructure.account.models import Account as AccountDjango
from accounts.infrastructure.repositories.exceptions import NotFoundError, RepositoryError


class AccountRepositoryDjango(AccountRepository):

    def get_by_id(self, id: int) -> AccountDomain:
        account: Optional[AccountDjango] = AccountDjango.objects.filter(pk=id).first()

        if not account:
            raise NotFoundError()

        return account.to_domain()

    def get_all_by_user_id(self, user_id: int) -> List[AccountDomain]:
        accounts: List[AccountDjango] = AccountDjango.objects.filter(owner_id=user_id)

        return [account.to_domain() for account in accounts]

    def save(self, account: AccountDomain) -> AccountDomain:
        try:
            AccountDjango.objects.update_or_create(id=account.id, amount=account.amount, owner_id=account.owner_id)
        except IntegrityError:
            raise RepositoryError()

        return account
