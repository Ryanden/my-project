from django.db import models

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
        related_name='carts'
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='carts'
    )

    product_amount = models.PositiveIntegerField(default=1)
