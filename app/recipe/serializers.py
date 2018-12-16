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

