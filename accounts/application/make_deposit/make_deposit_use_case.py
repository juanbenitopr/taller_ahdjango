from accounts.application.make_deposit.make_deposit_command import MakeDepositCommand
from accounts.domain.account import Account
from accounts.domain.repositories.account_repository import AccountRepository


class MakeDepositUseCase:

    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def execute(self, make_deposit_command: MakeDepositCommand) -> Account:
        account = self.account_repository.get_by_id(id=make_deposit_command.account_id)

        account.deposit(make_deposit_command.amount)

        return account
