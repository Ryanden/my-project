from django.db import models
from products.models import Product


class ProductOption(models.Model):
    name = models.CharField(max_length=200)

    description = models.TextField()

    price = models.PositiveIntegerField(default=0)

    count = models.PositiveIntegerField(default=0)

    product = models.ForeignKey(
        Product,
        blank=True,
        on_delete=models.CASCADE,
        related_name='product_options'
    )

    def __str__(self):
        return f'{self.name}'

    @property
    def product_name(self):
        return f'{self.product.title}'

