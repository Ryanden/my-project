from django import forms
from django.core.exceptions import ValidationError

from .models import ItemRegister, CostCalculator, Recipe


class ItemRegisterModelForm(forms.ModelForm):
    class Meta:
        model = ItemRegister
        fields = (
            'name',
            'capacity',
            'cost',
        )


class ItemRegisterForm(forms.Form):
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
        if ItemRegister.objects.filter(name=name).exists():
            raise ValidationError('이미 등록된 이름입니다.')
        return self.cleaned_data

    def register(self):
        fields = [
            'name',
            'capacity',
            'cost',
        ]

        create_item_dict = dict(filter(lambda item: item[0] in fields, self.cleaned_data.items()))

        item = ItemRegister.objects.create(**create_item_dict)
        return item


class RecipeForm(forms.Form):
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
    #     if Recipe.objects.filter(name=name).exists():
    #         raise ValidationError('이미 등록된 레시피입니다.')
    #     return self.cleaned_data
    #
    # def create(self):
    #     fields = [
    #         'name',
    #         'price',
    #     ]
    #
    #     create_recipe_dict = dict(filter(lambda item: item[0] in fields, self.cleaned_data.items()))
    #
    #     recipe = Recipe.objects.create(**create_recipe_dict)
    #     return recipe

    def save(self, user):
        return Recipe.objects.create(
            user=user,
            name=self.cleaned_data['name'],
            price=self.cleaned_data['price'],
        )


class CalculatorForm(forms.Form):
    item = forms.ModelChoiceField(
        label='이름',
        queryset=(
            ItemRegister.objects.all().order_by('name')
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
        item = self.cleaned_data.get('item')
        # if CostCalculator.objects.filter(item=item.pk).exists():
        #     raise ValidationError('이미 등록된 재료입니다.')
        return self.cleaned_data

    def register(self):
        fields = [
            'name',
            'capacity',
            'cost',
        ]

        create_item_dict = dict(filter(lambda item: item[0] in fields, self.cleaned_data.items()))

        item = ItemRegister.objects.create(**create_item_dict)
        return item

    def save(self, user):
        return CostCalculator.objects.create(
            user=user,
            item=self.cleaned_data['item'],
            usage=self.cleaned_data['usage'],
        )

# class CalculatorForm(forms.Form):
#     item = forms.ModelChoiceField(
#         label='이름',
#         queryset=(
#             ItemRegister.objects.all().order_by('name')
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
#         item = self.cleaned_data.get('item')
#         if CostCalculator.objects.filter(item=item.pk).exists():
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
#         create_item_dict = dict(filter(lambda item: item[0] in fields, self.cleaned_data.items()))
#
#         item = ItemRegister.objects.create(**create_item_dict)
#         return item
#
#     def save(self, user):
#         return CostCalculator.objects.create(
#             user=user,
#             item=self.cleaned_data['item'],
#             usage=self.cleaned_data['usage'],
#         )
