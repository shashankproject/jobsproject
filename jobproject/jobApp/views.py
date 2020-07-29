from django.shortcuts import render
from django.http import HttpResponse
from jobApp.models import *
# Create your views here.
def home(request):
    return render(request,'jobApp/home.html')

def hydjobsinfo(request):
    return render(request,'jobApp/hyd.html')

def bangjobsinfo(request):
    jobs_list=bangjobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'jobApp/bang.html',context=my_dict)


def chennaijobsinfo(request):
    return render(request,'jobApp/chennai.html')
