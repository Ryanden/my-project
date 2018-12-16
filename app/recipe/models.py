from django.db import models
from members.models import User


class Recipe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes'
    )
    name = models.CharField(max_length=200)

    type = models.CharField(max_length=200)

    capacity = models.TextField()

    manufacturing_method = models.TextField()

    packing_material = models.TextField()

    preservation_method = models.TextField()

    expiration_date = models.TextField()

    def __str__(self):
        return self.name
