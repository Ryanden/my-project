from rest_framework import serializers

from .models import Product, Ordering, OrderingInfo


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


class OrderingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordering

        fields = (
            'user',
            'product',
            'ordering_info',
        )


class OrderingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderingInfo

        fields = (
            'address1',
            'address2',
            'comment',
            'requested_at',
            'cancel_at',
        )
