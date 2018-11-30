from rest_framework import generics

from ..models import Product, Ordering, OrderingInfo
from ..serializers import ProductSerializer, OrderingSerializer, OrderingInfoSerializer


# ListCreateAPIView를 사용해서 Post Create를 Postman으로 실행해보기
# 관련 테스트 짜오기 (List 및 Create)
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderingList(generics.ListAPIView):
    queryset = Ordering.objects.all()
    serializer_class = OrderingSerializer


class OrderingInfoList(generics.ListAPIView):
    queryset = OrderingInfo.objects.all()
    serializer_class = OrderingInfoSerializer
