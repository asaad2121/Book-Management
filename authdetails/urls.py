from django.urls import path
from authdetails import views

urlpatterns= [ 
    path('', views.index , name = "index"),
    path('', views.index, name='search_results'),
    path('download/', views.download_as_csv , name = "download_as_csv"),
    #path('addauthor', views.authFormDetails , name = 'form name'),
]