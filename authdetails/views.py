from django.shortcuts import render
from .models import authorDet, bookDet
from django.views.generic.list import ListView
from django.db.models import Q
from .forms import authForm
from django.http import HttpResponse
import csv

def get_queryset(self): 
        query = self.request.GET.get("q")
        object_list= authorDet.objects.filter(
            Q(auth_name__icontains=query) | Q(auth_country__icontains=query)
        )
        return render(self, 'authordetails/index.html',)

def index(request):
    model = authorDet
    template_name = "authordetails/index.html"
            
    print(request.GET)
    query = request.GET.get("q","")
    dataDet= authorDet.objects.filter(  Q(auth_name__icontains=query) | Q(auth_country__icontains=query)  )
    # print(object_list)
    

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