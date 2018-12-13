from rest_framework import generics

from ..models import Product
from ..serializers import ProductSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def get_queryset(self):
    #     user = self.request.user
    #
    #     print(user, '실행ㅁㅁㅁㄴㅇㅁㄴㅇㅁㄴㅇㅁㄴㅇ ')
    #
    #     return Product.objects.filter(author=user)


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
