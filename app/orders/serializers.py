from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order

        fields = (
            'address1',
            'address2',
            'comment',
            'requested_at',
            'cancel_at',
        )
