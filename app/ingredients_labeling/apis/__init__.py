from django.shortcuts import get_list_or_404
from rest_framework import generics, permissions, status
from rest_framework.exceptions import NotAuthenticated
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from members.models import User

from ..models import Ingredient, IngredientsLabeling
from ..serializers import IngredientSerializer, IngredientsLabelingSerializer
from ..permission import IsUserOrReadOnly


# Ingredient api
class IngredientList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.list(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def get_queryset(self):
        queryset = get_list_or_404(Ingredient)

        return queryset

    serializer_class = IngredientSerializer


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class IngredientCreate(APIView):
    permission_classes = (IsAuthenticated,)
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def get(self, request):

        if request.user.is_authenticated:
            return Response(IngredientSerializer().data)
        raise NotAuthenticated('인증안됨')

    def post(self, request):

        if request.user.is_authenticated:
            ingredients_labeling = IngredientsLabeling.objects.get(pk=request.data['ingredients_labeling_pk'])

            ingredient = Ingredient.objects.create(
                ingredients_labeling=ingredients_labeling,
                name=request.data['name'],
                calorie=request.data['calorie'],
                capacity=request.data['capacity'],
                sodium=request.data['sodium'],
                carbohydrate=request.data['carbohydrate'],
                sugars=request.data['sugars'],
                fat=request.data['fat'],
                trans_fatty_acid=request.data['trans_fatty_acid'],
                saturated_fatty_acid=request.data['saturated_fatty_acid'],
                cholesterol=request.data.get('cholesterol'),
                protein=request.data.get('protein'),
            )

            return Response(IngredientSerializer(ingredient).data, status=status.HTTP_201_CREATED)
        raise NotAuthenticated('인증안됨')


# Ingredients Labeling api
class IngredientsLabelingList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.list(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def get_queryset(self):
        queryset = get_list_or_404(IngredientsLabeling)

        return queryset

    serializer_class = IngredientsLabelingSerializer


class IngredientsLabelingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IngredientsLabeling.objects.all()
    serializer_class = IngredientsLabelingSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class IngredientsLabelingCreate(APIView):
    permission_classes = (IsAuthenticated,)
    queryset = IngredientsLabeling.objects.all()
    serializer_class = IngredientsLabelingSerializer

    def get(self, request):

        if request.user.is_authenticated:
            return Response(IngredientsLabelingSerializer().data)
        raise NotAuthenticated('인증안됨')

    def post(self, request):

        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)

            ingredient_labeling = IngredientsLabeling.objects.create(
                user=user,
                name=request.data['name'],
                original_weight=request.data['original_weight'],
                product_weight=request.data['product_weight'],
                weight_change_rate=request.data['weight_change_rate'],
                total_weight=request.data['total_weight'],
                total_unit_count=request.data['total_unit_count'],
                single_unit_capacity=request.data['single_unit_capacity'],
                unit_type=request.data['unit_type'],
                unit_count_type=request.data['unit_count_type'],
                specific_gravity=request.data.get('specific_gravity'),
                gravity_weight=request.data.get('gravity_weight'),
            )

            return Response(IngredientsLabelingSerializer(ingredient_labeling).data, status=status.HTTP_201_CREATED)
        raise NotAuthenticated('인증안됨')
