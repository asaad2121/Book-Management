from django.urls import path
from authdetails import views

urlpatterns= [ 
    path('', views.index , name = "index"),
    #path('addauthor', views.authFormDetails , name = 'form name'),
]