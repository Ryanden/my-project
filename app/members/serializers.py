from django.contrib.auth import get_user_model
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
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

    def update(self, instance, validated_data):

        if validated_data.get('username'):
            print('user_name 은 보내지말것')
            return instance

        if validated_data.get('phone_number'):
            instance.phone_number = validated_data.get('phone_number')

        if validated_data.get('img_profile'):
            instance.img_profile = validated_data.get('img_profile')

        if validated_data.get('nickname'):
            instance.nickname = validated_data.get('nickname')

        instance.save()
        return instance

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
            nickname=validated_data['nickname'],
            phone_number=validated_data['phone_number'],
        )

        return validated_data
