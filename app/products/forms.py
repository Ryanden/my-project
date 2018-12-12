from django import forms
from .models import Product


class ProductModelForm(forms.ModelForm):
    # field정의를 직접 하지 않음
    #  (어떤 field를 사용할 것인지만 class Meta에 기록)
    class Meta:
        model = Product
        fields = (
            'title',
            'company',
            'type',
            'photos',
            'content',
            'base_shipping_charge',
            'free_shipping_charge_limit',
            'extra_shipping_charge',
        )


class ProductForm(forms.Form):

    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    company = forms.CharField(
        label='브랜드명',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    type = forms.CharField(
        label='제품유형',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    photos = forms.ImageField(
        label='사진',
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'multiple': True,
            }
        )
    )
    content = forms.CharField(
        label='제품설명',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    base_shipping_charge = forms.IntegerField(
        label='기본배송료',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    free_shipping_charge_limit = forms.IntegerField(
        label='무료배송료조건',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    extra_shipping_charge = forms.IntegerField(
        label='제주/도서산간지역 추가비용',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    def save(self, author):
        return Product.objects.create(
            author=author,
            title=self.cleaned_data['title'],
            company=self.cleaned_data['company'],
            type=self.cleaned_data['type'],
            photos=self.cleaned_data['photos'],
            content=self.cleaned_data['content'],
            base_shipping_charge=self.cleaned_data['base_shipping_charge'],
            free_shipping_charge_limit=self.cleaned_data['base_shipping_charge_limit'],
            extra_shipping_charge=self.cleaned_data['extra_shipping_charge'],
        )
