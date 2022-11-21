from django import forms
from authdetails.models import authorDet
class authForm(forms.ModelForm):
    class Meta:
        model = authorDet
        fields = '__all__'