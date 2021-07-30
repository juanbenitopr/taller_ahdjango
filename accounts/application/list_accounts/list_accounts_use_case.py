from accounts.application.list_accounts.list_accounts_command import ListAccountCommand
from accounts.domain.account import Account
from accounts.domain.repositories.account_repository import AccountRepository


class ListAccountUseCase:

    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def execute(self, list_accounts_command: ListAccountCommand) -> Account:
        return self.account_repository.get_by_id(id=list_accounts_command.owner_id)