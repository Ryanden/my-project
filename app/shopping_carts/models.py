from django.db import models

from lectures.models import Lecture
from products.models import Product
from members.models import User
from orders.models import Order


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='carts'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='carts',
        blank=True,
        null=True,
    )

    lecture = models.ForeignKey(
        Lecture,
        on_delete=models.CASCADE,
        related_name='carts',
        blank=True,
        null=True,
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='carts',
        blank=True,
        null=True,
    )

    product_amount = models.PositiveIntegerField(default=1)
