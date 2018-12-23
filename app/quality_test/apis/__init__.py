from django.shortcuts import get_list_or_404
from rest_framework import generics, permissions, status
from rest_framework.exceptions import NotAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import QualityTest, TestInstitution
from ..serializers import QualityTestSerializer, TestInstitutionSerializer
from ..permission import IsUserOrReadOnly


# quality_test api
class QualityTestList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.list(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def get_queryset(self):
        queryset = get_list_or_404(QualityTest)

        return queryset

    serializer_class = QualityTestSerializer


class QualityTestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QualityTest.objects.all()
    serializer_class = QualityTestSerializer
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


class QualityTestCreate(APIView):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsUserOrReadOnly,
        # IsAuthenticated,
    )
    queryset = QualityTest.objects.all()
    serializer_class = QualityTestSerializer

    def get(self, request):
        if request.user.is_authenticated:
            return Response(QualityTestSerializer().data)
        raise NotAuthenticated('인증안됨')

    def post(self, request):
        serializer = QualityTestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestInstitutionList(generics.ListAPIView):
    queryset = TestInstitution.objects.all()
    serializer_class = TestInstitutionSerializer


class TestInstitutionCreate(generics.CreateAPIView):
    queryset = TestInstitution.objects.all()
    serializer_class = TestInstitutionSerializer
