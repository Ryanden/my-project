from rest_framework import serializers

from .models import Ingredient, IngredientsLabeling


class IngredientsLabelingSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientsLabeling
        fields = (
            'pk',
            'user',
            'name',
            'original_weight',
            'product_weight',
            'weight_change_rate',
            'total_weight',
            'total_unit_count',
            'single_unit_capacity',
            'unit_type',
            'unit_count_type',
            'specific_gravity',
        )


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = (
            'pk',
            'ingredients_labeling',
            'name',
            'calorie',
            'capacity',
            'sodium',
            'carbohydrate',
            'sugars',
            'fat',
            'trans_fatty_acid',
            'saturated_fatty_acid',
            'cholesterol',
            'protein',
        )
