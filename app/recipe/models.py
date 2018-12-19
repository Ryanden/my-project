from django.db import models
from members.models import User


class Recipe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes'
    )
    name = models.CharField(max_length=200, verbose_name='레시피명')

    type = models.CharField(max_length=200, verbose_name='상품유형')

    capacity = models.TextField(verbose_name='내용량')

    manufacturing_method = models.TextField(verbose_name='제조방법')

    packing_material = models.TextField(verbose_name='포장방법')

    preservation_method = models.TextField(verbose_name='보존방법')

    expiration_date = models.TextField(verbose_name='유통기한')

    def __str__(self):
        return self.name
