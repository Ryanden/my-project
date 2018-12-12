# /api/users/
# 1. members.serializers -> UserSerializer
# 2. apis.__init__
#   class UserList(generics.ListAPIView):
#
# 3. config.urls에서
#   /api/users/ 가 위의 UserList.as_view()와 연결되도록 처리
from rest_framework import generics

from ..models import Product
from ..serializers import ProductSerializer


# ListCreateAPIView를 사용해서 Product Create를 Productman으로 실행해보기
# 관련 테스트 짜오기 (List 및 Create)
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
