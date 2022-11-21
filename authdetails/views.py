from django.shortcuts import render
from .models import authorDet, bookDet
from .forms import authForm
# Create your views here.
def index(request):
    dataDet = authorDet.objects.order_by("auth_age") 
    age_dict = {'authorDet': dataDet}
  
    form = authForm()
    if request.method == 'POST':
        form = authForm(request.POST)
        if form.is_valid():
            form.save()
            form = authForm()
            print("Form Valid")
        return render(request, 'authordetails/index.html',{'form':form, 'age_dict':age_dict, 'dataDet':dataDet})            
    else:
        form = authForm()
    return render(request, 'authordetails/index.html',{'form':form, 'age_dict':age_dict, 'dataDet':dataDet})         