from rest_framework import generics

from ..models import ProductOption
from ..serializers import ProductOptionSerializer


# ListCreateAPIView를 사용해서 Post Create를 Postman으로 실행해보기
# 관련 테스트 짜오기 (List 및 Create)
class ProductOptionList(generics.ListAPIView):
    queryset = ProductOption.objects.all()
    serializer_class = ProductOptionSerializer


class ProductOptionDetail(generics.RetrieveAPIView):
    queryset = ProductOption.objects.all()
    serializer_class = ProductOptionSerializer

