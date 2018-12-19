from django.db import models
from members.models import User
from recipe.models import Recipe


class TestInstitution(models.Model):
    name = models.CharField(max_length=200, verbose_name='업체명')

    address = models.CharField(max_length=200, verbose_name='주소')

    field = models.CharField(max_length=200, verbose_name='검사분야')

    phone_number = models.CharField(max_length=200, verbose_name='연락처')

    def __str__(self):
        return self.name


class QualityTest(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='quality_tests'
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='quality_tests',
        verbose_name='레시피'
    )

    institution = models.ForeignKey(
        TestInstitution,
        on_delete=models.CASCADE,
        related_name='quality_tests',
        verbose_name='검사업체'
    )
