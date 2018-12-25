from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from quality_test.models import TestInstitution

__all__ = (
    'quality_test_create',
)


def quality_test_create(request):
    companies = QualityInstitution.create_institution()

    print('검사업체 등록 요청')

    if TestInstitution.objects.count() < 1:

        for company in companies:
            TestInstitution.objects.create(
                name=company.name,
                address=company.address,
                field=company.field,
                phone_number=company.phone_number
            )

    count = TestInstitution.objects.count()

    print(f'{count}개가 등록되어있습니다.')

    return HttpResponse(f'기관 {count}개 등록완료')


class QualityInstitution:

    def __init__(self, name, address, field, phone_number):
        self.name = name
        self.address = address
        self.field = field
        self.phone_number = phone_number

    @classmethod
    def create_institution(cls):
        institutions = []

        name = [
            '축산물안전관리인증원',
            '한국식품산업협회 부설 한국식품과학연구원',
            '랩프런티어',
            '에이엔드에프',
            '삼성웰스토리(주) 식품연구소',
            '농협중앙회 축산연구원',
            '계명대학교 전통미생물자원연구센터',
        ]
        address = [
            '경기도 안양시 만안구 전파로24번길 55',
            '서울특별시 서초구 명달로 4',
            '경기도 안양시 동안구 안양천동로 60 영린빌딩 3층',
            '경기도 안산시 단원구 광덕4로 250 씨티프라자 5층',
            '경기도 용인시 기흥구 용구대로 2442-1',
            '경기도 안성시 공도읍 대신두길 42-20',
            '대구광역시 달서구 달구벌대로 1095 계명대학교 첨단산업지원센터 103호',
        ]
        field = [
            '이화학(중금속제외), 미생물',
            '이화학, 미생물, 잔류농약, 동물용의약품',
            '이화학, 미생물',
            '이화학, 미생물',
            '이화학, 미생물',
            '이화학, 미생물, 잔류농약, 잔류동물용의약품(합성호르몬제외)',
            '이화학, 미생물',
        ]
        phone_number = [
            '031-390-5252',
            '02-3470-8200',
            '031-460-9125',
            '031-493-3547',
            '031-899-0543',
            '031-659-1336',
            '053-580-6441',
        ]

        for i in range(7):
            institutions.append(QualityInstitution(
                name=name[i],
                address=address[i],
                field=field[i],
                phone_number=phone_number[i]
            ))

        return institutions
