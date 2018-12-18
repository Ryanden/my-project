from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from ..models import Recipe
from ..serializers import RecipeSerializer


# recipe api
class RecipeList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Recipe.objects.filter(user=self.request.user)

        return queryset

    serializer_class = RecipeSerializer


# class RecipeList(generics.ListAPIView):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer


class RecipeDetail(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeCreate(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        print(self.request.user)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # queryset = Recipe.objects.all()
    def get_queryset(self):
        queryset = Recipe.objects.filter(user=self.request.user)

        return queryset
    serializer_class = RecipeSerializer
    permissions = (permissions.IsAuthenticated,)


class RecipePatch(generics.UpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDelete(generics.DestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
