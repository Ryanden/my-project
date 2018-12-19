from rest_framework import serializers

from .models import CostCalculator, Material, Item


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = (
            'pk',
            'name',
            'capacity',
            'cost',

        )


class CostCalculatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCalculator
        fields = (
            'pk',
            'user',
            'material',
            'usage',
        )


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'pk',
            'user',
            'name',
            'prime_cost',
            'price',
            'margin',
            'profit',
            'count',
        )

