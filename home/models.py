from django.conf import settings
from django.db import models


class Holdings(models.Model):
    "Generated Model"
    symbol = models.CharField(
        blank=True,
        max_length=256,
    )
    purchaseDate = models.DateField(
        blank=True,
    )
    uniqueId = models.BigIntegerField(
        null=True,
        blank=True,
    )
    purchasePrice = models.DecimalField(
        null=True,
        blank=True,
        max_digits=30,
        decimal_places=10,
    )
    accountId = models.BigIntegerField(
        null=True,
        blank=True,
    )


class Accounts(models.Model):
    "Generated Model"
    uniqueId = models.BigIntegerField()
    accountNumber = models.CharField(
        max_length=256,
    )
    accountName = models.BigIntegerField()
    openDate = models.DateField()
    closeDate = models.DateField()
