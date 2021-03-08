from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import Line


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class NewLine(forms.ModelForm):
    class Meta:
        model = Line
        fields = ['name', 'phone', 'line_date', 'line_time']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Имя *'
                }),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Номер телефона *'
                }),
            'line_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }),
            'line_time': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'time'
                })
        }
