from django import forms
from django.core.exceptions import ValidationError

from .models import Recipe


class RecipeModelForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'name',
            'user',
            'type',
            'capacity',
            'method',
            'packing_material',
            'expiration_date',
        )


class RecipeForm(forms.Form):
    name = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    type = forms.CharField(
        label='식품유형',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    capacity = forms.CharField(
        label='원재료 및 함유량',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    method = forms.CharField(
        label='제조방법',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    packing_material = forms.CharField(
        label='포장재질',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    expiration_date = forms.CharField(
        label='유통기한',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    def clean(self):
        super().clean()
        name = self.cleaned_data['name']
        if Recipe.objects.filter(name=name).exists():
            raise ValidationError('이미 등록된 이름입니다.')
        return self.cleaned_data

    def register(self):
        fields = [
            'name',
            'user',
            'type',
            'capacity',
            'method',
            'packing_material',
            'expiration_date',
        ]

        create_recipe_dict = dict(filter(lambda item: item[0] in fields, self.cleaned_data.items()))

        recipe = Recipe.objects.create(**create_recipe_dict)
        return recipe
