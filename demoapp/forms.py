from django import forms
from .models import *
from django.contrib.auth.models import User


class DemoForm(forms.ModelForm):
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    age = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Demo
        fields = '__all__'
        exclude = ('status', )


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = UserRegister
        fields = '__all__'
        exclude = ('user',)
