from rest_framework import generics

from ..models import Lecture
from ..serializers import LectureSerializer


class LectureList(generics.ListAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


class LectureDetail(generics.RetrieveAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
