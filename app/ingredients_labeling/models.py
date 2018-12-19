from django.db import models
from members.models import User


class IngredientsLabeling(models.Model):
    UNIT_TYPE_GRAM = 'g'
    UNIT_TYPE_ML = 'ml'
    CHOICES_UNIT_TYPE = (
        (UNIT_TYPE_GRAM, '그램'),
        (UNIT_TYPE_ML, '밀리리터'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ingredients_labeling'
    )
    name = models.CharField(max_length=200, verbose_name='제품명')

    # 초기중량
    original_weight = models.PositiveIntegerField(default=0, verbose_name='초기중량(g)')

    # 제조후 중량
    product_weight = models.PositiveIntegerField(default=0, verbose_name='제조후중량(g)')

    # 중량변화율
    weight_change_rate = models.FloatField(default=0, verbose_name='중량변화율(%)')

    # 총 내용량
    total_weight = models.PositiveIntegerField(default=0, verbose_name='총내용량(g)')

    # 제품 전체 개수
    total_unit_count = models.PositiveIntegerField(default=0, verbose_name='단위수')

    # 한개 단위 내용량
    single_unit_capacity = models.PositiveIntegerField(default=0, verbose_name='단위내용량')

    # ml 인지 g 인지
    unit_type = models.CharField(max_length=2, choices=CHOICES_UNIT_TYPE, verbose_name='단위')

    # 세는 단위
    unit_count_type = models.CharField(max_length=200, default='1개', verbose_name='세는 단위')

    # 비중
    specific_gravity = models.FloatField(default=0, verbose_name='비중')

    # 무게
    gravity_weight = models.PositiveIntegerField(default=0, verbose_name='무게')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    ingredients_labeling = models.ForeignKey(
        IngredientsLabeling,
        on_delete=models.CASCADE,
        related_name='ingredients',
        blank=True,
        verbose_name='영양성분표'
    )

    name = models.CharField(max_length=200, verbose_name='이름')

    calorie = models.PositiveIntegerField(default=0, verbose_name='칼로리')

    capacity = models.PositiveIntegerField(default=0, verbose_name='용량')

    # 나트륨
    sodium = models.FloatField(default=0, verbose_name='나트륨')

    # 탄수화물
    carbohydrate = models.FloatField(default=0, verbose_name='탄수화물')

    # 당류
    sugars = models.FloatField(default=0, verbose_name='당류')

    # 지방
    fat = models.FloatField(default=0, verbose_name='지방')

    # 트랜스지방
    trans_fatty_acid = models.FloatField(default=0, verbose_name='트랜스지방')

    # 포화지방
    saturated_fatty_acid = models.FloatField(default=0, verbose_name='포화지방')

    # 콜레스테롤
    cholesterol = models.FloatField(default=0, verbose_name='콜레스테롤')

    # 단백질
    protein = models.FloatField(default=0, verbose_name='단백질')

    # 임의표시 영양성분
    # 식이섬유
    dietary_fiber = models.FloatField(default=0)

    vitamin_a = models.FloatField(default=0)

    # 비타민 B1 티아민
    thiamine = models.FloatField(default=0)

    # 비타민 B2 리보플라빈
    riboflavin = models.FloatField(default=0)

    # 나이아신
    niacin = models.FloatField(default=0)

    # 판토텐산
    pantothenic_acid = models.FloatField(default=0)

    # 비타민 B6 피리독신
    pyridoxine = models.FloatField(default=0)

    # 비오틴
    biotin = models.FloatField(default=0)

    # 비타민 B9 엽산
    folic_acid = models.FloatField(default=0)

    # 비타민 B12 사이아노코발라민
    cyanocobalamin = models.FloatField(default=0)

    vitamin_c = models.FloatField(default=0)

    vitamin_d = models.FloatField(default=0)

    vitamin_e = models.FloatField(default=0)

    vitamin_k = models.FloatField(default=0)

    # 칼슘
    calcium = models.FloatField(default=0)

    # 인
    phosphorus = models.FloatField(default=0)

    # 칼륨
    potassium = models.FloatField(default=0)

    # 마그네슘
    magnesium = models.FloatField(default=0)

    # 철분
    iron = models.FloatField(default=0)

    # 아연
    zinc = models.FloatField(default=0)

    # 구리
    copper = models.FloatField(default=0)

    # 망간
    manganese = models.FloatField(default=0)

    # 요오드
    iodine = models.FloatField(default=0)

    # 셀렌
    selenium = models.FloatField(default=0)

    # 몰리브덴
    molybdenum = models.FloatField(default=0)

    # 크롬
    chromium = models.FloatField(default=0)

    # 기타영양성분
    # 알콜
    alcohol = models.FloatField(default=0)

    # 유기산
    organic_acid = models.FloatField(default=0)

    # 당알코올
    sugar_alcohol = models.FloatField(default=0)

    # 에리스리톨
    erythritol = models.FloatField(default=0)

    # 타가토스
    tagatose = models.FloatField(default=0)

    # 알룰로스
    allulose = models.FloatField(default=0)

    def __str__(self):
        return self.name
