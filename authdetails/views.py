from django.shortcuts import render
from .models import authorDet, bookDet
from django.views.generic.list import ListView
from django.db.models import Q
from .forms import authForm, booksForm
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookDetailsSerializer,BookAuthorDetailsSerializer
import csv
import datetime


def is_valid_queryparam(param):
    return param != '' and param is not None

def bookView(request):
    model = bookDet
    template_name = "authordetails/books.html"

    query = request.GET.get("q","")
    dataDet= bookDet.objects.filter(  Q(book_name__icontains=query) )
    rating = request.GET.get('rating')
    year_count_min = request.GET.get('year_count_min')
    year_count_max = request.GET.get('year_count_max')
    page_count_min = request.GET.get('page_count_min')
    page_count_max = request.GET.get('page_count_max')
    

    if is_valid_queryparam(rating) and rating != 'Select':
        dataDet = dataDet.filter(average_critics_rating=rating)

    if is_valid_queryparam(year_count_min):
        dataDet = dataDet.filter(book_date__gte=datetime.date(int(year_count_min), 1,1))
        
    if is_valid_queryparam(year_count_max):
        dataDet = dataDet.filter(book_date__lt=datetime.date(int(year_count_max), 12, 31))
    
    if is_valid_queryparam(page_count_min):
        dataDet = dataDet.filter(book_pages__gte=page_count_min)
        
    if is_valid_queryparam(page_count_max):
        dataDet = dataDet.filter(book_pages__lt=page_count_max)

    form = booksForm()
    if request.method == 'POST':
        form = booksForm(request.POST)
        if form.is_valid():
            form.save()
            form = booksForm()
            print("Form Valid")
        return render(request, 'authordetails/books.html',{'form':form, 'dataDet':dataDet})            
    else:
        form = booksForm()
    return render(request, 'authordetails/books.html',{'form':form, 'dataDet':dataDet})         

def index(request):
    model = authorDet
    template_name = "authordetails/index.html"
    
    query = request.GET.get("q",'')
    authors_age = request.GET.get('age_input')
    age_count_min = request.GET.get('age_count_min')
    age_count_max = request.GET.get('age_count_max')
    genders = request.GET.get('genders')
    
    dataDet= authorDet.objects.filter(  Q(auth_name__icontains=query) | Q(auth_country__icontains=query)  )    
    if is_valid_queryparam(age_count_min):
        dataDet = dataDet.filter(auth_age__gte=age_count_min)

    if is_valid_queryparam(age_count_max):
        dataDet = dataDet.filter(auth_age__lt=age_count_max)

    if is_valid_queryparam(genders) and genders != 'Select':
        dataDet = dataDet.filter(auth_gender=genders)
        
    form = authForm()
    if request.method == 'POST':
        form = authForm(request.POST)
        if form.is_valid():
            form.save()
            form = authForm()
            print("Form Valid")
        return render(request, 'authordetails/index.html',{'form':form, 'dataDet':dataDet})            
    else:
        form = authForm()
    return render(request, 'authordetails/index.html',{'form':form, 'dataDet':dataDet})         


def download_as_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Authors.csv' 
    
    writer = csv.writer(response)
    writer.writerow(['Name','Age','Gender','Country'])
    
    # expenses = queryset_filter(User.objects.get(username=request.user.username),filter_by).order_by('date')
    authors = authorDet.objects.filter()
    for auth in authors:
        writer.writerow([auth.auth_name, auth.auth_age, auth.auth_gender, auth.auth_country.name])
    
    return response

def download_as_csv_books(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Books.csv' 
    
    writer = csv.writer(response)
    writer.writerow(['Name','Author','Date','Pages', 'Ratings'])
    
    # expenses = queryset_filter(User.objects.get(username=request.user.username),filter_by).order_by('date')
    booksF = bookDet.objects.filter()
    for bok in booksF:
        writer.writerow([bok.book_name, bok.book_author, bok.book_date, bok.book_pages, bok.average_critics_rating])
    
    return response

@api_view(['GET'])
def get_author_books(request):
    author_name = request.GET.get("author_name",None)
    if(author_name == None or author_name == ""):
        return Response({"error":"Please give author_name as get parameter"},status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            author = authorDet.objects.get(auth_name = author_name)
            books = bookDet.objects.filter(book_author= author)
            serializer = BookDetailsSerializer(books,many = True)
            return Response(serializer.data)
        except authorDet.DoesNotExist:
            return Response({"error":"Author does not exist."},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"error":"Something went wrong"},status=status.HTTP_400_BAD_REQUEST)
            

@api_view(['GET'])
def get_gte_average_critics_rating(request):
    average_critics_rating = request.GET.get("average_critics_rating",None)
    if(average_critics_rating == None or average_critics_rating == ""):
        return Response({"error":"Please give average_critics_rating as get parameter"},status=status.HTTP_400_BAD_REQUEST)
    else:
        average = 0
        try:
            average = int(average_critics_rating)
        except:
            return Response({"error":"Please give a number in average_critics_rating"},status=status.HTTP_400_BAD_REQUEST)

        try:
            books = bookDet.objects.filter(average_critics_rating__gte = average)
            serializer = BookAuthorDetailsSerializer(books,many = True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response({"error":"Something went wrong"},status=status.HTTP_400_BAD_REQUEST)
            
