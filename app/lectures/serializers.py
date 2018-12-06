from rest_framework import serializers

from .models import Lecture


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = (
            'pk',
            'lecture_name',
            'lecture_option',
            'lecture_price',
            'lecture_total_count',
        )
