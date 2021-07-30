from django.core.handlers.asgi import ASGIRequest

# Create your views here.
from accounts.application.retrieve_account.retrieve_account_use_case import RetrieveAccountAmountUseCase
from accounts.domain.repositories.account_repository import AccountRepository
from accounts.infrastructure.repositories.account_repository_django import AccountRepositoryDjango


class AccountAPI:

    def retrieve(self, request: ASGIRequest, id: str):
        account_repository: AccountRepository = AccountRepositoryDjango()

        RetrieveAccountAmountUseCase(account_repository)