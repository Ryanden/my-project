from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'pk',
            'author',
            'title',
            'company',
            'type',
            'photos',
            'content',
            'base_shipping_charge',
            'free_shipping_charge_limit',
            'extra_shipping_charge',
            'created_at',
            'tags',
            'like_users',
            'comments',
            'inquiries',
        )
