# /api/users/
# 1. members.serializers -> UserSerializer
# 2. apis.__init__
#   class UserList(generics.ListAPIView):
#
# 3. config.urls에서
#   /api/users/ 가 위의 UserList.as_view()와 연결되도록 처리
from rest_framework import generics

from ..models import Store
from ..serializers import StoreSerializer


# ListCreateAPIView를 사용해서 Store Create를 Storeman으로 실행해보기
# 관련 테스트 짜오기 (List 및 Create)
class StoreList(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class StoreDetail(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
