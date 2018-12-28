from django.shortcuts import get_list_or_404
from rest_framework import generics, permissions, status
from rest_framework.exceptions import NotAuthenticated

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView

from members.models import User
from ..models import BookMark
from ..serializers import BookMarkSerializer
from ..permission import IsUserOrReadOnly


# recipe api
class BookMarkList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.list(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def get_queryset(self):
        queryset = get_list_or_404(BookMark, user=self.request.user)

        return queryset

    serializer_class = BookMarkSerializer


class BookMarkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookMark.objects.all()
    serializer_class = BookMarkSerializer
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


class BookMarkCreate(APIView):
    permission_classes = (IsAuthenticated,)
    queryset = BookMark.objects.all()
    serializer_class = BookMarkSerializer

    def get(self, request):
        # URL: /api/users/profile/
        # request.user가 인증되어 있으면
        #   UserSerializer로 serialize한 결과를 리턴
        # 인증 안되어있으면 NotAuthenticated예외 발생
        if request.user.is_authenticated:
            return Response(BookMarkSerializer().data)
        raise NotAuthenticated('인증안됨')

    def post(self, request):

        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)

            recipe = BookMark.objects.create(
                user=user,
                name=request.data['name'],
                link=request.data['link'],
                price=request.data['price'],
                image=request.data['image'],

            )

            return Response(BookMarkSerializer(recipe).data, status=status.HTTP_201_CREATED)
        raise NotAuthenticated('인증안됨')
