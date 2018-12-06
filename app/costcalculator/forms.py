from django import forms

from .models import ItemRegister, CostCalculator


class ItemRegisterModelForm(forms.ModelForm):
    class Meta:
        model = ItemRegister
        fields = (
            'name',
            'capacity',
            'cost',
        )


class CalculatorModelForm(forms.ModelForm):
    class Meta:
        model = CostCalculator
        fields = (
            'user',
            'item',
            'usage',
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

    def save(self):
        return ItemRegister.objects.create(
            name=self.cleaned_data['name'],
            capacity=self.cleaned_data['capacity'],
            cost=self.cleaned_data['cost'],
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

    def save(self, user):
        return CostCalculator.objects.create(
            user=user,
            item=self.cleaned_data['item'],
            usage=self.cleaned_data['usage'],
        )
