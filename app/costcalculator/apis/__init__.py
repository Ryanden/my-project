from rest_framework import generics

from ..models import Ingredient, CostCalculator
from ..serializers import IngredientSerializer, CostCalculatorSerializer


class IngredientList(generics.ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientDetail(generics.RetrieveAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class CostCalculatorList(generics.ListAPIView):
    queryset = CostCalculator.objects.all()
    serializer_class = CostCalculatorSerializer


class CostCalculatorDetail(generics.RetrieveAPIView):
    queryset = CostCalculator.objects.all()
    serializer_class = CostCalculatorSerializer
