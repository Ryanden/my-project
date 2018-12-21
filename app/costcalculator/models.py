from django.db import models
from members.models import User


class Material(models.Model):
    name = models.CharField(max_length=200, verbose_name='재료명')

    capacity = models.PositiveIntegerField(default=0, verbose_name='용량')

    cost = models.PositiveIntegerField(default=0, verbose_name='가격')

    cost_per_one = models.IntegerField(default=0, verbose_name='1g당 가격')

    def __str__(self):
        return self.name


class Item(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='items',
    )
    name = models.CharField(max_length=200, verbose_name='제품명')

    prime_cost = models.PositiveIntegerField(default=0, verbose_name='원가')

    price = models.PositiveIntegerField(default=0, verbose_name='판매가격')

    margin = models.FloatField(default=0, verbose_name='마진')

    profit = models.IntegerField(default=0, verbose_name='이익')

    count = models.PositiveIntegerField(default=1, verbose_name='판매개수')

    def __str__(self):
        return self.name


class CostCalculator(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='calculators'
    )

    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name='calculators',
        verbose_name='재료'
    )

    usage = models.PositiveIntegerField(default=1)
