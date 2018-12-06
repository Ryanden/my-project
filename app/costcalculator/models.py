from django.db import models
from members.models import User


class ItemRegister(models.Model):
    name = models.CharField(max_length=200)

    capacity = models.PositiveIntegerField(default=0)

    cost = models.PositiveIntegerField(default=0)

    cost_per_one = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class CostCalculator(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='calculators'
    )

    item = models.ForeignKey(
        ItemRegister,
        on_delete=models.CASCADE,
        related_name='calculators',
    )

    usage = models.PositiveIntegerField(default=1)
