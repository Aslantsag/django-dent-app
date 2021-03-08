from django import forms
from main.models import Line
from users.models import UserMedia, UserPrice, UserInfo
from dent.lang_dict import lang_dict as l


class MediaForm(forms.ModelForm):
    class Meta:
        model = UserMedia
        fields = ['file', 'title']
        widgets = {
            'file': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }),
            'title': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '5',
                    'placeholder': l['common_title']
                })
        }


class PriceForm(forms.ModelForm):
    class Meta:
        model = UserPrice
        fields = ['title', 'price']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': l['common_title']
                }),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': l['price_title']
                })
        }


class InfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['user_image', 'about_text', 'phone', 'insta', 'whats', 'geo', 'address']
        widgets = {
            'user_image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }),
            'about_text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': l['about_text']
                }),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': l['enter_phone']
                }),
            'insta': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': l['enter_insta']
                }),
            'whats': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': l['enter_whats']
                }),
            'geo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': l['enter_geo']
                }),
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': l['enter_address']
                })
        }