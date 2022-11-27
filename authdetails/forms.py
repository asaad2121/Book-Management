from django import forms
from authdetails.models import authorDet, bookDet   
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

class booksForm(forms.ModelForm):
    class Meta:
        model = bookDet
        fields = "__all__"
        widgets={
            'book_name' : forms.TextInput(attrs={
                'placeholder': 'Book Name',
                'class': 'form-control'
                }),
            'book_author' : forms.Select(attrs={
                'class': 'form-control'
            }),
            'book_date': forms.SelectDateWidget(attrs={
                'placeholder': 'Book Date',
                'class': 'form-control',
                'width' : '20rem'
            }),
            'book_pages': forms.TextInput(attrs={
                'placeholder': 'Book Pages',
                'class': 'form-control'
                }),
            'average_critics_rating' :forms.DateInput(attrs={
                'placeholder': 'Book Rating',
                'class': 'form-control'
            }),
        }