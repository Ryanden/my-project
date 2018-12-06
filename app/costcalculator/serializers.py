from rest_framework import serializers

from .models import CostCalculator, ItemRegister


class ItemRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemRegister
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
            'item',
            'usage',
        )
