from accounts.application.retrieve_account.retrieve_account_command import RetrieveAccountCommand
from accounts.domain.account import Account
from accounts.domain.repositories.account_repository import AccountRepository


class RetrieveAccountAmountUseCase:

    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def execute(self, retrieve_account_command: RetrieveAccountCommand) -> Account:
        return self.account_repository.get_by_id(id=retrieve_account_command.account_id)