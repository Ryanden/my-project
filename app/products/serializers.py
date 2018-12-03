from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'pk',
            'product_name',
            'product_option',
            'product_price',
            'product_total_count',
        )
