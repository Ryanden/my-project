from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from members.models import User


class Store(models.Model):
    ON = 'YA'
    OFF = 'NA'

    STORE_STATUS = (
        (ON, 'Yes'),
        (OFF, 'No'),
    )
    store_name = models.CharField(max_length=100)

    store_type = models.CharField(max_length=100)

    store_company_name = models.CharField(max_length=100)

    store_img = models.CharField(max_length=200)

    store_detail_img = models.CharField(max_length=200)

    store_interested_count = models.PositiveIntegerField(blank=True, default=0)

    store_is_funding = models.CharField(
        max_length=3,
        choices=STORE_STATUS,
        default=ON
    )

    store_description = models.TextField(blank=True)

    store_like_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='like_product'
    )

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ['-pk']


class StoreLike(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='like_products'
    )

    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    liked_at = models.DateTimeField(auto_now_add=True)

    # @property
    # def product_name(self):
    #     return f'{self.product.product_name}'
    #
    # @property
    # def product_type(self):
    #     return f'{self.product.product_type}'
    #
    # @property
    # def product_company_name(self):
    #     return f'{self.product.product_company_name}'
    #
    # @property
    # def product_img(self):
    #     return f'{self.product.product_img}'
    #
    # @property
    # def product_interested_count(self):
    #     return f'{self.product.product_interested_count}'
    #
    # @property
    # def product_is_funding(self):
    #     return f'{self.product.product_is_funding}'
    #
    # @property
    # def user_name(self):
    #     return f'{self.user.username}'


class Product(models.Model):
    product_name = models.CharField(max_length=200)

    product_option = models.TextField()

    product_price = models.PositiveIntegerField(default=0)

    product_shipping_charge = models.PositiveIntegerField(default=0)

    product_total_count = models.PositiveIntegerField(default=0)

    product_sold_count = models.PositiveIntegerField(default=0)

    product_on_sale = models.BooleanField(default=True)

    store = models.ForeignKey(
        Store,
        blank=True,
        on_delete=models.CASCADE,
        related_name='rewards'
    )

    def __str__(self):
        return f'{self.product_name}'


class OrderingInfo(models.Model):
    username = models.CharField(max_length=20)

    phone_regex = RegexValidator(regex='\d{11}',
                                 message="Phone number must be 11 numbers")
    phone_number = models.CharField(validators=[phone_regex], max_length=11, blank=True)

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
        related_name='funding'
    )

    ordering_info = models.ForeignKey(
        OrderingInfo,
        on_delete=models.CASCADE,
        related_name='order'
    )

    reward_amount = models.PositiveIntegerField(default=1)


class Comment(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    parent_comment = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='comments'
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    contents = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    modified_at = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment (post: {self.store.pk}, user: {self.user.username})'

    @property
    def author(self):
        if self.is_deleted:
            return None
        return self.user

    @property
    def content(self):
        if self.is_deleted:
            return '삭제된 덧글 입니다.'
        return self.content

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()
