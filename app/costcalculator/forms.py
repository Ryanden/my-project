from django import forms
from django.core.exceptions import ValidationError

from .models import Ingredient, CostCalculator, Item


class IngredientModelForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = (
            'name',
            'capacity',
            'cost',
        )


class IngredientForm(forms.Form):
    name = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    capacity = forms.CharField(
        label='용량',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    cost = forms.CharField(
        label='가격',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    def clean(self):
        super().clean()
        name = self.cleaned_data['name']
        if Ingredient.objects.filter(name=name).exists():
            raise ValidationError('이미 등록된 이름입니다.')
        return self.cleaned_data

    def register(self):
        fields = [
            'name',
            'capacity',
            'cost',
        ]

        create_ingredient_dict = dict(filter(lambda item: item[0] in fields, self.cleaned_data.items()))

        ingredient = Ingredient.objects.create(**create_ingredient_dict)
        return ingredient


class ItemForm(forms.Form):
    name = forms.CharField(
        label='판매제품',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'style': 'width:100%;',
            }
        )
    )

    price = forms.CharField(
        label='판매가격',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'style': 'width:100%;'
            }
        )
    )

    # def clean(self):
    #     super().clean()
    #     name = self.cleaned_data['name']
    #     if Item.objects.filter(name=name).exists():
    #         raise ValidationError('이미 등록된 레시피입니다.')
    #     return self.cleaned_data
    #
    # def create(self):
    #     fields = [
    #         'name',
    #         'price',
    #     ]
    #
    #     create_item_dict = dict(filter(lambda item: item[0] in fields, self.cleaned_data.items()))
    #
    #     item = Item.objects.create(**create_item_dict)
    #     return item

    def save(self, user):
        return Item.objects.create(
            user=user,
            name=self.cleaned_data['name'],
            price=self.cleaned_data['price'],
        )


class CalculatorForm(forms.Form):
    ingredient = forms.ModelChoiceField(
        label='이름',
        queryset=(
            Ingredient.objects.all().order_by('name')
        ),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'style': 'width:200px;',
            }
        )
    )

    usage = forms.CharField(
        label='용량',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'style': 'width:50px;'
            }
        )
    )

    def clean(self):
        super().clean()

        print(self.cleaned_data)
        ingredient = self.cleaned_data.get('ingredient')
        # if CostCalculator.objects.filter(ingredient=ingredient.pk).exists():
        #     raise ValidationError('이미 등록된 재료입니다.')
        return self.cleaned_data

    def register(self):
        fields = [
            'name',
            'capacity',
            'cost',
        ]

        create_ingredient_dict = dict(filter(lambda item: item[0] in fields, self.cleaned_data.items()))

        ingredient = Ingredient.objects.create(**create_ingredient_dict)
        return ingredient

    def save(self, user):
        return CostCalculator.objects.create(
            user=user,
            ingredient=self.cleaned_data['ingredient'],
            usage=self.cleaned_data['usage'],
        )

# class CalculatorForm(forms.Form):
#     ingredient = forms.ModelChoiceField(
#         label='이름',
#         queryset=(
#             Ingredient.objects.all().order_by('name')
#         ),
#         widget=forms.Select(
#             attrs={
#                 'class': 'form-control',
#                 'style': 'width:200px;',
#             }
#         )
#     )
#
#     usage = forms.CharField(
#         label='용량',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'style': 'width:50px;'
#             }
#         )
#     )
#
#     def clean(self):
#         super().clean()
#
#         print(self.cleaned_data)
#         ingredient = self.cleaned_data.get('ingredient')
#         if CostCalculator.objects.filter(ingredient=ingredient.pk).exists():
#             raise ValidationError('이미 등록된 재료입니다.')
#         return self.cleaned_data
#
#     def register(self):
#         fields = [
#             'name',
#             'capacity',
#             'cost',
#         ]
#
#         create_ingredient_dict = dict(filter(lambda item: item[0] in fields, self.cleaned_data.items()))
#
#         ingredient = Ingredient.objects.create(**create_ingredient_dict)
#         return ingredient
#
#     def save(self, user):
#         return CostCalculator.objects.create(
#             user=user,
#             ingredient=self.cleaned_data['ingredient'],
#             usage=self.cleaned_data['usage'],
#         )
