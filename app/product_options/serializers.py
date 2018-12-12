from rest_framework import serializers

from .models import ProductOption


class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = (
            'pk',
            'name',
            'description',
            'price',
            'count',
        )
