from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class Account(models.Model):
    amount = models.FloatField()
    owner = models.ForeignKey(User, on_delete=CASCADE)
