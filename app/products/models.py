from django.db import models
from members.models import User
from stores.models import Store


class Product(models.Model):
    product_name = models.CharField(max_length=200)

    product_option = models.TextField()

    product_price = models.PositiveIntegerField(default=0)

    product_total_count = models.PositiveIntegerField(default=0)

    store = models.ForeignKey(
        Store,
        blank=True,
        on_delete=models.CASCADE,
        related_name='products'
    )

    def __str__(self):
        return f'{self.product_name}'

    @property
    def store_name(self):
        return f'{self.store.title}'

