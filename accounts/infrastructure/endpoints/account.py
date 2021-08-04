from django.core.handlers.asgi import ASGIRequest

# Create your views here.
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

from accounts.application.make_deposit.make_deposit_command import MakeDepositCommand
from accounts.application.make_deposit.make_deposit_use_case import MakeDepositUseCase
from accounts.application.retrieve_account.retrieve_account_command import RetrieveAccountCommand
from accounts.application.retrieve_account.retrieve_account_use_case import RetrieveAccountAmountUseCase
from accounts.infrastructure.repositories.account_repository_django import AccountRepositoryDjango
from accounts.infrastructure.serializers.account import AccountSerializer
from accounts.infrastructure.serializers.deposit import DepositSerializer


class AccountAPI:

    def __init__(self):
        self.account_repository = AccountRepositoryDjango()

    @method_decorator(require_GET)
    def retrieve(self, request: ASGIRequest, account_id: int) -> JsonResponse:
        user_case = RetrieveAccountAmountUseCase(self.account_repository)

        command = RetrieveAccountCommand(account_id=account_id)
        account = user_case.execute(command)

        account_serializer = AccountSerializer.from_orm(account)

        return JsonResponse(account_serializer.dict())

    @method_decorator(require_POST)
    @method_decorator(csrf_exempt)
    def deposit(self, request: ASGIRequest, account_id: int):
        user_case = MakeDepositUseCase(self.account_repository)

        deposit_serializer = DepositSerializer(account_id=account_id, amount=request.POST.get('amount'))
        command = MakeDepositCommand(account_id=deposit_serializer.account_id, amount=deposit_serializer.amount)

        account = user_case.execute(command)

        account_serializer = AccountSerializer.from_orm(account)

        return JsonResponse(account_serializer.dict())
