from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'reg_input',
            'placeholder': 'Введите логин'})
        self.fields['first_name'].widget.attrs.update({
            'class': 'reg_input',
            'placeholder': 'Введите ваше имя'})
        self.fields['email'].widget.attrs.update({
            'class': 'reg_input',
            'placeholder': 'Введите вашу почту'})
        self.fields['password'].widget.attrs.update({
            'class': 'reg_input',
            'placeholder': 'Введите пароль'})
        self.fields['password2'].widget.attrs.update({
            'class': 'reg_input',
            'placeholder': 'Повторите пароль'})

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['country', 'city', 'date_of_birth', 'photo']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['country'].label = 'Страна'
        self.fields['city'].label = 'Город'
        self.fields['date_of_birth'].label = 'Дата рождения'
        self.fields['photo'].label = 'Фотография профиля'


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'reg_input',
            'placeholder': 'Введите логин'})
        
        self.fields['password'].widget.attrs.update({
            'class': 'reg_input',
            'placeholder': 'Введите пароль'})