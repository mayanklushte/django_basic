from django import forms
from .models import *


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
