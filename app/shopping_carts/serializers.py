from rest_framework import serializers

from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart

        fields = (
            'user',
            'product_option',
            'order',
            'product_option_amount',
        )

