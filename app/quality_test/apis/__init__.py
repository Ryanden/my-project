from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from ..models import QualityTest, TestInstitution
from ..serializers import QualityTestSerializer, TestInstitutionSerializer


# quality_test api
class QualityTestList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = QualityTest.objects.filter(user=self.request.user)

        return queryset

    serializer_class = QualityTestSerializer


# class QualityTestList(generics.ListAPIView):
#     queryset = QualityTest.objects.all()
#     serializer_class = QualityTestSerializer


class QualityTestDetail(generics.RetrieveAPIView):
    queryset = QualityTest.objects.all()
    serializer_class = QualityTestSerializer


class QualityTestCreate(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = QualityTest.objects.filter(user=self.request.user)

        return queryset

    def get(self, request, *args, **kwargs):
        print(self.request.user)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):


        return self.create(request, *args, **kwargs)

    serializer_class = QualityTestSerializer
    permissions = (permissions.IsAuthenticated,)


class QualityTestPatch(generics.UpdateAPIView):
    queryset = QualityTest.objects.all()
    serializer_class = QualityTestSerializer


class QualityTestDelete(generics.DestroyAPIView):
    queryset = QualityTest.objects.all()
    serializer_class = QualityTestSerializer


class TestInstitutionList(generics.ListAPIView):
    queryset = TestInstitution.objects.all()
    serializer_class = TestInstitutionSerializer


class TestInstitutionCreate(generics.CreateAPIView):
    queryset = TestInstitution.objects.all()
    serializer_class = TestInstitutionSerializer
