import unittest

from accounts.domain.account import Account
from accounts.domain.user import User


class TestAccount(unittest.TestCase):

    def test_deposit_is_working(self):
        account = Account(id=1, amount=5, owner=User(id=1))

        self.assertEqual(account.deposit(10), 15)
        self.assertEqual(account.amount, 15)
