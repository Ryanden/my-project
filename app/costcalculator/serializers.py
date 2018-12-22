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

    def create(self, validated_data):
        print('안에는 뭐가들었나?', validated_data)

        cost_per_one = int(validated_data['cost']) / int(validated_data['capacity'])

        Material.objects.create(
            name=validated_data['name'],
            capacity=validated_data['capacity'],
            cost=validated_data['cost'],
            cost_per_one=cost_per_one,
        )

        return validated_data


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
