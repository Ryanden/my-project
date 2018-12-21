from django.shortcuts import get_list_or_404
from rest_framework import generics, permissions, status
from rest_framework.exceptions import NotAuthenticated

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView

from members.models import User
from ..models import Recipe
from ..serializers import RecipeSerializer
from ..permission import IsUserOrReadOnly


# recipe api
class RecipeList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.list(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def get_queryset(self):
        queryset = get_list_or_404(Recipe, user=self.request.user)

        return queryset

    serializer_class = RecipeSerializer


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsUserOrReadOnly,
    )

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class RecipeCreate(APIView):
    permission_classes = (IsAuthenticated,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get(self, request):
        # URL: /api/users/profile/
        # request.user가 인증되어 있으면
        #   UserSerializer로 serialize한 결과를 리턴
        # 인증 안되어있으면 NotAuthenticated예외 발생
        if request.user.is_authenticated:
            return Response(RecipeSerializer().data)
        raise NotAuthenticated('인증안됨')

    def post(self, request):

        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)

            recipe = Recipe.objects.create(
                user=user,
                name=request.data['name'],
                type=request.data['type'],
                capacity=request.data['capacity'],
                manufacturing_method=request.data['manufacturing_method'],
                packing_material=request.data['packing_material'],
                preservation_method=request.data['preservation_method'],
                expiration_date=request.data['expiration_date'],
            )

            return Response(RecipeSerializer(recipe).data, status=status.HTTP_201_CREATED)
        raise NotAuthenticated('인증안됨')
