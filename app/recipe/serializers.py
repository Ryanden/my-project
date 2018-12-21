from rest_framework import serializers

from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'pk',
            'name',
            'user',
            'type',
            'capacity',
            'manufacturing_method',
            'packing_material',
            'preservation_method',
            'expiration_date',
        )

    def create(self, validated_data):
        print('안에는 뭐가들었나?', validated_data)
        # Recipe.objects.create(
        #     name=validated_data['name'],
        #     type=validated_data['type'],
        #     capacity=validated_data['capacity'],
        #     manufacturing_method=validated_data['manufacturing_method'],
        #     packing_material=validated_data['packing_material'],
        #     preservation_method=validated_data['preservation_method'],
        #     expiration_date=validated_data['expiration_date'],
        # )

        return validated_data

