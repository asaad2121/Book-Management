from django import forms
from authdetails.models import authorDet
from django_countries.fields import CountryField
class authForm(forms.ModelForm):
    class Meta:
        GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
        )
        model = authorDet
        fields = '__all__'
        widgets={
            'auth_name' : forms.TextInput(attrs={
                'placeholder': 'Author Name',
                'class': 'form-control'
                }),
            'auth_age' : forms.TextInput(attrs={
                'placeholder': 'Author Age',
                'class': 'form-control'
                }),
            'auth_gender' : forms.Select(attrs={
                'class': 'form-control'
            }),
            'auth_country' : forms.Select(attrs={
                'class': 'form-control'
            })
            
        }