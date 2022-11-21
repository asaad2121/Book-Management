from django.db import models
from django_countries.fields import CountryField
# from .utils import GenderTypes


class authorDet(models.Model):
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    auth_name = models.CharField(max_length=30, unique=True)
    auth_age = models.IntegerField()    
    auth_gender = models.CharField( max_length=1, choices=GENDER_CHOICES)
    auth_country = CountryField()

    def get_gender_type_label(self):
        return GenderTypes(self.auth_gender).name.title()

    def __str__(self):
        return self.auth_name

class bookDet(models.Model):
    book_name = models.CharField(max_length=60, unique=True)
    book_author = models.ForeignKey("authorDet", on_delete=models.CASCADE)
    book_date = models.DateField() 
    book_pages = models.IntegerField()
    average_critics_rating = models.IntegerField()

    def __str__(self):
        return self.book_name
