from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import SET_NULL

from accounts.domain.account import Account as AccountDomain


class Account(models.Model):
    amount = models.FloatField()
    owner = models.ForeignKey(User, on_delete=SET_NULL)

    def to_domain(self) -> AccountDomain:
        return AccountDomain(id=self.id, amount=self.amount, owner_id=int(self.owner_id))
