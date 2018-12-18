from rest_framework import serializers

from .models import QualityTest, TestInstitution


class QualityTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityTest
        fields = (
            'pk',
            'user',
            'recipe',
            'institution',
        )


class TestInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestInstitution
        fields = (
            'pk',
            'name',
            'field',
            'phone_number',

        )
