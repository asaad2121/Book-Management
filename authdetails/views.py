from django.shortcuts import render
from .models import authorDet, bookDet
from django.views.generic.list import ListView
from django.db.models import Q
from .forms import authForm

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