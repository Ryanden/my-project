from rest_framework import serializers

from .models import CostCalculator, Ingredient, Item


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
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
            'ingredient',
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

