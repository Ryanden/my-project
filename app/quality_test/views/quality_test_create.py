from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

__all__ = (
    'quality_test_create',
)


def quality_test_create(request):
    institution = []

    return HttpResponse('aa')


class QualityInstitution:

    def __init__(self, name, address, field, phone_number):
        self.name = name
        self.address = address
        self.field = field
        self.phone_number = phone_number

    def create_institution(self):
        institutions = []

        name = ['한국식품과학연구원', '한국식품과학연구원부산지소', '한국기초과학연구원서울센터']
        address = ['경기도 의왕시 붓들로 50(포일동)', '부산시 남구 수영로 309(대연동)', '서울시 성북구 안암로 145 고려대학교 자연캠퍼스']
        field = ['이화학, 미생물, 잔류농약, 잔류동물용의약품, 유전자변형식품의 확인검사, 식품조사처리확인',
                 '이화학, 미생물, 잔류농약, 잔류동물용의약품, 유전자변형식품의 확인검사']
        phone_number = ['02-3470-8200', '051-628-7953', '02-6943-4197']

        for name, address, field, phone_number in institutions:
            QualityInstitution(
                name=name,
                address=address,
                field=field,
                phone_number=phone_number
            )
        return
