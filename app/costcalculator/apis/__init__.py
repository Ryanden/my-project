from django.shortcuts import get_list_or_404
from rest_framework import generics, permissions, status
from rest_framework.exceptions import NotAuthenticated
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from members.models import User
from ..models import Material, CostCalculator, Item
from ..serializers import MaterialSerializer, CostCalculatorSerializer, ItemSerializer
from ..permission import IsUserOrReadOnly


# material api

class MaterialList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.list(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def get_queryset(self):
        queryset = get_list_or_404(Material)

        return queryset

    serializer_class = MaterialSerializer


class MaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
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


class MaterialCreate(APIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsUserOrReadOnly,
        # IsAuthenticated,
    )
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    def get(self, request):
        if request.user.is_authenticated:
            return Response(MaterialSerializer().data)
        raise NotAuthenticated('인증안됨')

    def post(self, request):
        serializer = MaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# calculator api
class CostCalculatorList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.list(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def get_queryset(self):
        queryset = get_list_or_404(CostCalculator, user=self.request.user)

        return queryset

    serializer_class = CostCalculatorSerializer


class CostCalculatorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CostCalculator.objects.all()
    serializer_class = CostCalculatorSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsUserOrReadOnly,
    )

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CostCalculatorCreate(APIView):
    permission_classes = (IsAuthenticated,)
    queryset = CostCalculator.objects.all()
    serializer_class = CostCalculatorSerializer

    def get(self, request):

        if request.user.is_authenticated:
            return Response(CostCalculatorSerializer().data)
        raise NotAuthenticated('인증안됨')

    def post(self, request):

        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)

            item = Item.objects.get(pk=request.data['item_pk'])

            material = Material.objects.get(name=request.data['material'])

            calculator = CostCalculator.objects.create(
                user=user,
                material=material,
                item=item,
                usage=int(request.data['usage']),
            )

            return Response(CostCalculatorSerializer(calculator).data, status=status.HTTP_201_CREATED)
        raise NotAuthenticated('인증안됨')


# item api

class ItemList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.list(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def get_queryset(self):
        queryset = get_list_or_404(Item, user=self.request.user)

        return queryset

    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsUserOrReadOnly,
    )

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemCreate(APIView):
    permission_classes = (IsAuthenticated,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request):

        if request.user.is_authenticated:
            return Response(ItemSerializer().data)
        raise NotAuthenticated('인증안됨')

    def post(self, request):

        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)
            item = Item.objects.create(
                user=user,
                name=request.data['name'],
                price=int(request.data['price']),
            )

            return Response(ItemSerializer(item).data, status=status.HTTP_201_CREATED)
        raise NotAuthenticated('인증안됨')


