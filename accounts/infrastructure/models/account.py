from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE

from accounts.domain.account import Account as AccountDomain


class Account(models.Model):
    amount = models.FloatField(default=0)
    owner = models.ForeignKey(User, on_delete=CASCADE)

    def to_domain(self) -> AccountDomain:
        return AccountDomain(id=self.id, amount=self.amount, owner_id=int(self.owner_id))