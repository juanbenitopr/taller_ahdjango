from django.contrib.auth.models import User
from django.test import TestCase

from accounts.infrastructure.models import Account


class TestAccountDeposit(TestCase):

    def setUp(self) -> None:
        self.owner = User.objects.create_user(username='test_1')
        self.account = Account.objects.create(owner_id=self.owner.pk)

    def test_deposit_is_working_fine(self):
        deposit_body = {
            'amount': 10
        }
        response = self.client.post(f'/accounts/{self.account.pk}/deposit', data=deposit_body)

        self.assertEqual(response.status_code, 200)

        response_json = response.json()
        self.assertEqual(response_json['owner_id'], self.owner.pk)
        self.assertEqual(response_json['amount'], 10)
