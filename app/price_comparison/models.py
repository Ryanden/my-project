from django.db import models
from members.models import User


class BookMark(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookmarks',
    )
    name = models.CharField(max_length=200, verbose_name='제품명')

    link = models.CharField(max_length=1000, verbose_name='제품링크')

    price = models.CharField(max_length=200,verbose_name='제품가격')

    image = models.CharField(max_length=200, verbose_name='제품이미지')

    def __str__(self):
        return self.name
