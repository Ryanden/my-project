from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from members.models import User
from stores.models import Store


# class Store(models.Model):
#     ON = 'YA'
#     OFF = 'NA'
#
#     STORE_STATUS = (
#         (ON, 'Yes'),
#         (OFF, 'No'),
#     )
#     store_name = models.CharField(max_length=100)
#
#     store_type = models.CharField(max_length=100)
#
#     store_company_name = models.CharField(max_length=100)
#
#     store_img = models.CharField(max_length=200)
#
#     store_detail_img = models.CharField(max_length=200)
#
#     store_interested_count = models.PositiveIntegerField(blank=True, default=0)
#
#     store_is_funding = models.CharField(
#         max_length=3,
#         choices=STORE_STATUS,
#         default=ON
#     )
#
#     store_description = models.TextField(blank=True)
#
#     store_like_user = models.ManyToManyField(
#         settings.AUTH_USER_MODEL,
#         blank=True,
#         related_name='like_product'
#     )
#
#     def __str__(self):
#         return self.store_name
#
#     class Meta:
#         ordering = ['-pk']


# class StoreLike(models.Model):
#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name='like_products'
#     )
#
#     store = models.ForeignKey(
#         Store,
#         on_delete=models.CASCADE,
#         related_name='likes'
#     )
#
#     liked_at = models.DateTimeField(auto_now_add=True)


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


class OrderingInfo(models.Model):

    address1 = models.CharField(max_length=30)

    address2 = models.CharField(max_length=30)

    comment = models.TextField()

    requested_at = models.DateTimeField(auto_now_add=True)

    cancel_at = models.DateTimeField(null=True)


class Ordering(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='ordering'
    )

    ordering_info = models.ForeignKey(
        OrderingInfo,
        on_delete=models.CASCADE,
        related_name='ordering'
    )

    product_amount = models.PositiveIntegerField(default=1)
