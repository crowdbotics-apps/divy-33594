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


class Drip(models.Model):
    "Generated Model"
    holdingId = models.BigIntegerField()
    dripStart = models.DateField()
    dripEnd = models.DateField()
    uniqueId = models.BigIntegerField(
        null=True,
        blank=True,
    )


class HoldingValue(models.Model):
    "Generated Model"
    holdingId = models.BigIntegerField()
    newShares = models.DecimalField(
        null=True,
        blank=True,
        max_digits=30,
        decimal_places=10,
    )
    uniqueId = models.BigIntegerField(
        null=True,
        blank=True,
    )


class Dividends(models.Model):
    "Generated Model"
    symbol = models.CharField(
        max_length=256,
    )
    exDate = models.DateField()
    payDate = models.DateField()
    declareDate = models.DateField()
    value = models.DecimalField(
        max_digits=30,
        decimal_places=10,
    )
    shares = models.DecimalField(
        max_digits=30,
        decimal_places=10,
    )
    uniqueId = models.BigIntegerField(
        null=True,
        blank=True,
    )


class ClosingValue(models.Model):
    "Generated Model"
    uniqueId = models.BigIntegerField()
    date = models.DateField()
    symbolId = models.BigIntegerField()
    closePrice = models.DecimalField(
        max_digits=30,
        decimal_places=10,
    )
