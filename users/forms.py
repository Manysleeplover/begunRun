from django.contrib.auth.models import User
from django import forms
from django.forms import EmailInput, PasswordInput, TextInput
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'username': TextInput(attrs={
                'class': 'input',
                'type': 'text',
                'required': 'TRUE'
            }),

            'password': PasswordInput(attrs={
                'class': 'input',
                'type': 'password',
                'required': 'TRUE'
            })
        }


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        widgets = {

            'email': EmailInput(attrs={
                'class': 'input',
                'required': 'TRUE'
            }),

            'username': TextInput(attrs={
                'class': 'input',
                'required': 'TRUE'
            }),


            'password': PasswordInput(attrs={
                'class': 'input',
                'type': 'password',
                'required': 'TRUE'
            }),

            'password2': PasswordInput(attrs={
                'class': 'input',
                'type': 'password',
                'required': 'TRUE'
            })
        }


        def clean_password2(self):
            cd = self.clean_data
            if cd['password'] != cd[ 'password2' ]:
                raise forms.ValidationError('Пароли не совпадают')


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'username',)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo', 'date_of_birth',
                    'country', 'city', 'gender', 'weight',
                    'height', 'profile_description')
