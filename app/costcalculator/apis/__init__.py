from rest_framework import generics

from ..models import ItemRegister, CostCalculator
from ..serializers import ItemRegisterSerializer, CostCalculatorSerializer


class ItemRegisterList(generics.ListAPIView):
    queryset = ItemRegister.objects.all()
    serializer_class = ItemRegisterSerializer


class ItemRegisterDetail(generics.RetrieveAPIView):
    queryset = ItemRegister.objects.all()
    serializer_class = ItemRegisterSerializer


class CostCalculatorList(generics.ListAPIView):
    queryset = CostCalculator.objects.all()
    serializer_class = CostCalculatorSerializer


class CostCalculatorDetail(generics.RetrieveAPIView):
    queryset = CostCalculator.objects.all()
    serializer_class = CostCalculatorSerializer
