from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from ..models import Ingredient, IngredientsLabeling
from ..serializers import IngredientSerializer, IngredientsLabelingSerializer


# Ingredient api
class IngredientList(generics.ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientDetail(generics.RetrieveAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientCreate(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientPatch(generics.UpdateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientDelete(generics.DestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


# Ingredients Labeling api
class IngredientsLabelingList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = IngredientsLabeling.objects.filter(user=self.request.user)

        return queryset

    serializer_class = IngredientsLabelingSerializer


class IngredientsLabelingDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = IngredientsLabeling.objects.filter(user=self.request.user)

        return queryset

    serializer_class = IngredientsLabelingSerializer


class IngredientsLabelingCreate(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = IngredientsLabeling.objects.filter(user=self.request.user)

        return queryset

    serializer_class = IngredientsLabelingSerializer


class IngredientsLabelingPatch(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = IngredientsLabeling.objects.filter(user=self.request.user)

        return queryset

    serializer_class = IngredientsLabelingSerializer


class IngredientsLabelingDelete(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = IngredientsLabeling.objects.filter(user=self.request.user)

        return queryset

    serializer_class = IngredientsLabelingSerializer
