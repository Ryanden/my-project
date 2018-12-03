from rest_framework import generics

from ..models import Product
from ..serializers import ProductSerializer


# ListCreateAPIView를 사용해서 Post Create를 Postman으로 실행해보기
# 관련 테스트 짜오기 (List 및 Create)
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

