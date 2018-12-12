from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class SignupModelForm(forms.ModelForm):
    pass


class SignupForm(forms.Form):
    user_id = forms.EmailField(
        label='아이디',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    username = forms.CharField(
        label='닉네임',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    tel_number = forms.CharField(
        label='전화번호',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    img_profile = forms.FileField(
        label='프로필 이미지',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
            }
        ),
        required=False,
    )
    introduce = forms.CharField(
        label='소개',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        ),
        required=False,
    )
    site = forms.URLField(
        label='사이트URL',
        widget=forms.URLInput(
            attrs={
                'class': 'form-control',
            }
        ),
        required=False,
    )

    store_name = forms.CharField(
        label='스토어이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
    )

    def clean_user_id(self):

        user_id = self.cleaned_data['user_id']
        if User.objects.filter(user_id=user_id).exists():
            raise ValidationError('이미 사용중인 아이디입니다')
        return user_id

    def clean_username(self):
        # username field의 clean()실행 결과가 self.cleaned_data['username']에 있음
        username = self.cleaned_data['username']

        if User.objects.filter(username=username).exists():
            raise ValidationError('이미 사용중인 닉네임입니다')
        return username

    def clean(self):
        super().clean()
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            self.add_error('password2', '비밀번호와 비밀번호확인의 값이 일치하지 않습니다')
        return self.cleaned_data

    def signup(self):
        # self.cleaned_data = {
        #     'username': 'value',
        #     'password': 'value',
        #     'password2': 'value',
        #     ...
        # }
        fields = [
            'user_id',
            'username',
            'password',
            'tel_number',
            'img_profile',
            'introduce',
            'site',
            'store_name',
        ]
        create_user_dict = {}
        for key, value in self.cleaned_data.items():
            if key in fields:
                create_user_dict[key] = value

        # dict comprehension으로
        create_user_dict = {key: value for key, value in self.cleaned_data.items() if key in fields}

        # filter를 사용
        def in_fields(item):
            return item[0] in fields

        # self.cleaned_data.items() = (('username', 'lhy10'), ('password', '123'), ('password2', '123'))
        result = filter(in_fields, self.cleaned_data.items())
        create_user_dict = {}
        for item in result:
            create_user_dict[item[0]] = item[1]

        # filter결과를 dict함수로 묶어서 새 dict생성
        create_user_dict = dict(filter(in_fields, self.cleaned_data.items()))
        create_user_dict = dict(filter(lambda item: item[0] in fields, self.cleaned_data.items()))

        user = User.objects.create_user(**create_user_dict)
        # username = self.cleaned_data['username']
        # email = self.cleaned_data['email']
        # password = self.cleaned_data['password']
        # gender = self.cleaned_data['gender']
        # img_profile = self.cleaned_data['img_profile']
        # introduce = self.cleaned_data['introduce']
        # site = self.cleaned_data['site']
        #
        # user = User.objects.create_user(
        #     username=username,
        #     email=email,
        #     password=password,
        #     gender=gender,
        #     img_profile=img_profile,
        #     introduce=introduce,
        #     site=site,
        # )
        return user
