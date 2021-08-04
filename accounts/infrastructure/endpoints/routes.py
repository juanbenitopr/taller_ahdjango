from django.urls import path

from accounts.infrastructure.endpoints.account import AccountAPI

account_api = AccountAPI()

routes = [
    path('<int:account_id>', account_api.retrieve),
    path('<int:account_id>/deposit', account_api.deposit)
]