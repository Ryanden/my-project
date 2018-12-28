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

from bs4 import BeautifulSoup
from selenium import webdriver
import time


# 크롤러
class Crawler:
    res_dict = {
        'name': '',
        'link': '',
        'price': '',
    }

    res_list = []

    @classmethod
    def get_data(cls, keyword):

        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome('price_comparison/driver/chromedriver', chrome_options=chrome_options)

        url = f'https://search.shopping.naver.com/search/all.nhn?query={keyword}'

        driver.get(url)

        time.sleep(10)

        html = driver.page_source

        soup = BeautifulSoup(html, 'lxml')

        ul_contents = soup.select("ul.goods_list li")

        for li in ul_contents:

            if li.select_one('div.info a') is not None:
                name = li.select_one('div.info a').get_text(strip=True)

                link = li.select_one('div.info a').get('href')
                cls.res_dict['name'] = name
                cls.res_dict['link'] = link

            if li.select_one('span.price em span') is not None:
                price = li.select_one('span.price em span').get_text(strip=True)

                cls.res_dict['price'] = price

                # if li.select_one('img') is not None:
                #     image = li.select_one('img').get('src')
                #     cls.res_dict['image'] = image

                cls.res_list.append(cls.res_dict.copy())
        driver.close()


# bookmark api
class SearchItemList(APIView):
    permission_classes = (IsAuthenticated,)
    queryset = BookMark.objects.all()
    serializer_class = BookMarkSerializer

    def get(self, request):
        if request.user.is_authenticated:
            Crawler.res_list.clear()
            Crawler.get_data(request.query_params.get('keyword'))

            return Response(Crawler.res_list)
        raise NotAuthenticated('인증안됨')

    def post(self, request):

        if request.user.is_authenticated:
            user = User.objects.get(username=request.user)

            recipe = BookMark.objects.create(
                user=user,
                name=request.data['name'],
                link=request.data['link'],
                price=request.data['price'],
            )

            return Response(BookMarkSerializer(recipe).data, status=status.HTTP_201_CREATED)
        raise NotAuthenticated('인증안됨')


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
            )

            return Response(BookMarkSerializer(recipe).data, status=status.HTTP_201_CREATED)
        raise NotAuthenticated('인증안됨')
