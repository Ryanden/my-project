from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'user_id',
            'username',
            'tel_number',
            'img_profile',
            'introduce',
            'site',
            'like_products',
            'carts',
            'recipes',
            'items',


        )



