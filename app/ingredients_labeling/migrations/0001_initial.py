# Generated by Django 2.1.2 on 2018-12-23 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='이름')),
                ('calorie', models.PositiveIntegerField(default=0, verbose_name='칼로리')),
                ('capacity', models.PositiveIntegerField(default=0, verbose_name='용량')),
                ('sodium', models.FloatField(default=0, verbose_name='나트륨')),
                ('carbohydrate', models.FloatField(default=0, verbose_name='탄수화물')),
                ('sugars', models.FloatField(default=0, verbose_name='당류')),
                ('fat', models.FloatField(default=0, verbose_name='지방')),
                ('trans_fatty_acid', models.FloatField(default=0, verbose_name='트랜스지방')),
                ('saturated_fatty_acid', models.FloatField(default=0, verbose_name='포화지방')),
                ('cholesterol', models.FloatField(default=0, verbose_name='콜레스테롤')),
                ('protein', models.FloatField(default=0, verbose_name='단백질')),
                ('dietary_fiber', models.FloatField(default=0)),
                ('vitamin_a', models.FloatField(default=0)),
                ('thiamine', models.FloatField(default=0)),
                ('riboflavin', models.FloatField(default=0)),
                ('niacin', models.FloatField(default=0)),
                ('pantothenic_acid', models.FloatField(default=0)),
                ('pyridoxine', models.FloatField(default=0)),
                ('biotin', models.FloatField(default=0)),
                ('folic_acid', models.FloatField(default=0)),
                ('cyanocobalamin', models.FloatField(default=0)),
                ('vitamin_c', models.FloatField(default=0)),
                ('vitamin_d', models.FloatField(default=0)),
                ('vitamin_e', models.FloatField(default=0)),
                ('vitamin_k', models.FloatField(default=0)),
                ('calcium', models.FloatField(default=0)),
                ('phosphorus', models.FloatField(default=0)),
                ('potassium', models.FloatField(default=0)),
                ('magnesium', models.FloatField(default=0)),
                ('iron', models.FloatField(default=0)),
                ('zinc', models.FloatField(default=0)),
                ('copper', models.FloatField(default=0)),
                ('manganese', models.FloatField(default=0)),
                ('iodine', models.FloatField(default=0)),
                ('selenium', models.FloatField(default=0)),
                ('molybdenum', models.FloatField(default=0)),
                ('chromium', models.FloatField(default=0)),
                ('alcohol', models.FloatField(default=0)),
                ('organic_acid', models.FloatField(default=0)),
                ('sugar_alcohol', models.FloatField(default=0)),
                ('erythritol', models.FloatField(default=0)),
                ('tagatose', models.FloatField(default=0)),
                ('allulose', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientsLabeling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='제품명')),
                ('original_weight', models.PositiveIntegerField(default=0, verbose_name='초기중량(g)')),
                ('product_weight', models.PositiveIntegerField(default=0, verbose_name='제조후중량(g)')),
                ('weight_change_rate', models.FloatField(default=0, verbose_name='중량변화율(%)')),
                ('total_weight', models.PositiveIntegerField(default=0, verbose_name='총내용량(g)')),
                ('total_unit_count', models.PositiveIntegerField(default=0, verbose_name='단위수')),
                ('single_unit_capacity', models.PositiveIntegerField(default=0, verbose_name='단위내용량')),
                ('unit_type', models.CharField(choices=[('g', '그램'), ('ml', '밀리리터')], max_length=2, verbose_name='단위')),
                ('unit_count_type', models.CharField(default='1개', max_length=200, verbose_name='세는 단위')),
                ('specific_gravity', models.FloatField(default=0, verbose_name='비중')),
                ('gravity_weight', models.PositiveIntegerField(default=0, verbose_name='무게')),
            ],
        ),
    ]
