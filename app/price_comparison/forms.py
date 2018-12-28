from django import forms
from django.core.exceptions import ValidationError

from .models import BookMark


class BookMarkModelForm(forms.ModelForm):
    class Meta:
        model = BookMark
        fields = (
            'user',
            'name',
            'link',
            'price',
            'image',
        )


class BookMarkForm(forms.Form):
    name = forms.CharField(
        label='제품명',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    link = forms.CharField(
        label='제품링크',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    price = forms.CharField(
        label='제품가격',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    image = forms.CharField(
        label='제품이미지',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    def clean(self):
        super().clean()
        name = self.cleaned_data['name']
        if BookMark.objects.filter(name=name).exists():
            raise ValidationError('이미 등록된 이름입니다.')
        return self.cleaned_data

    def register(self):
        fields = [
            'name',
            'user',
            'link',
            'price',
            'image',
        ]

        create_bookmark_dict = dict(filter(lambda item: item[0] in fields, self.cleaned_data.items()))

        bookmark = BookMark.objects.create(**create_bookmark_dict)
        return bookmark
