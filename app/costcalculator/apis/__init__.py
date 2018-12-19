from rest_framework import generics

from members.models import User
from ..models import Material, CostCalculator, Item
from ..serializers import MaterialSerializer, CostCalculatorSerializer, ItemSerializer


# material api

class MaterialList(generics.ListAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialDetail(generics.RetrieveAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialCreate(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


# calculator api
class CostCalculatorList(generics.ListAPIView):
    queryset = CostCalculator.objects.all()
    serializer_class = CostCalculatorSerializer


class CostCalculatorDetail(generics.RetrieveAPIView):
    queryset = CostCalculator.objects.all()
    serializer_class = CostCalculatorSerializer


class CostCalculatorCreate(generics.ListCreateAPIView):
    queryset = CostCalculator.objects.all()
    serializer_class = CostCalculatorSerializer


# item api

class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # def post(self, request, *args, **kwargs):
    #
    #     # 모든정보는 request.data 안에 담겨있다. 이내용을 save 하기전에 정보를 수장하여 저장하자.
    #     user_pk = request.data['user']
    #     prime_cost = request.data['prime_cost']
    #     price = request.data['price']
    #     margin = request.data['margin']
    #     profit = request.data['profit']
    #
    #     # 전달받은 user pk를 통해 user instance 를 생성
    #     user = User.objects.get(pk=user_pk)
    #
    #     # 유저인스턴스가 등록한
    #     Item.objects.filter(user=user)
    #
    #     print(request.data)
    #
    #     return self.create(request, *args, **kwargs)