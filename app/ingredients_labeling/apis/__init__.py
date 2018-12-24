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
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsUserOrReadOnly,
        # IsAuthenticated,
    )
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def get(self, request):
        if request.user.is_authenticated:
            return Response(IngredientSerializer().data)
        raise NotAuthenticated('인증안됨')

    def post(self, request):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

            # item = Item.objects.get(pk=request.data['item_pk'])
            #
            # material = Material.objects.get(name=request.data['material'])

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
