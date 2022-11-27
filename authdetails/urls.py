from django.urls import path
from authdetails import views

urlpatterns= [ 
    path('', views.index , name = "index"),
    path('', views.index, name='search_results'),
    path('download/', views.download_as_csv , name = "download_as_csv"),
    path('bdownload/', views.download_as_csv_books , name = "download_as_csv_books"),
    path('books',views.bookView, name="book_view"),
    path('books', views.bookView, name='book_search_results'),
    path('author-book-details', views.get_author_books, name='get_author_books'),
    path('critics-rating-books', views.get_gte_average_critics_rating, name='get_gte_average_critics_rating'),
]