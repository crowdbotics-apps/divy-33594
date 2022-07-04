from django.conf import settings
from django.db import models


class Holdings(models.Model):
    "Generated Model"
    symbol = models.CharField(
        max_length=256,
        blank=True,
    )
    purchaseDate = models.DateField(
        blank=True,
    )
    uniqueId = models.BigIntegerField(
        null=True,
        blank=True,
    )
    purchasePrice = models.DecimalField(
        max_digits=30,
        decimal_places=10,
        null=True,
        blank=True,
    )
    accountId = models.BigIntegerField(
        null=True,
        blank=True,
    )
