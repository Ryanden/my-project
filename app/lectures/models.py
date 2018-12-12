from django.db import models
from products.models import Product


class Lecture(models.Model):
    lecture_name = models.CharField(max_length=200)

    lecture_option = models.TextField()

    lecture_price = models.PositiveIntegerField(default=0)

    lecture_total_count = models.PositiveIntegerField(default=0)

    product = models.ForeignKey(
        Product,
        blank=True,
        on_delete=models.CASCADE,
        related_name='lectures'
    )

    def __str__(self):
        return f'{self.lecture_name}'

    @property
    def product_name(self):
        return f'{self.product.title}'

