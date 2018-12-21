from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    username = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(
        max_length=12, min_length=1, allow_blank=False, write_only=True)
    nickname = serializers.CharField(
        max_length=20, validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'nickname',
            'password',
            'phone_number',
            'img_profile',
            'like_products',
            'carts',
            'recipes',
            'items',
        )

    # def validate_password(self, value):
    #     print('value츌력', self.initial_data)
    #     if value == self.initial_data.get('check_password'):
    #         return value
    #     raise ValidationError('(password, check_password) 불일치')

    def create(self, validated_data):
        print('안에는 뭐가들었나?', validated_data)
        User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return validated_data
