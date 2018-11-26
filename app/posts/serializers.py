from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
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
        )