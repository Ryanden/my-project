from rest_framework import generics

from ..models import ProductOption
from ..serializers import ProductOptionSerializer


class ProductOptionList(generics.ListAPIView):
    serializer_class = ProductOptionSerializer
    queryset = ProductOption.objects.all()

    # def get_queryset(self):
    #
    #     user = self.request.user
    #
    #     return ProductOption.objects.filter()





class ProductOptionDetail(generics.RetrieveAPIView):
    queryset = ProductOption.objects.all()
    serializer_class = ProductOptionSerializer


# create
class ProductOptionCreate(generics.ListCreateAPIView):
    queryset = ProductOption.objects.all()
    serializer_class = ProductOptionSerializer
