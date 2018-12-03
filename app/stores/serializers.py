from rest_framework import serializers

from .models import Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = (
            'pk',
            'author',
            'title',
            'company',
            'product_type',
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
