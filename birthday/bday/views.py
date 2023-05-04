from django.shortcuts import render
import json
from .data import data
from .models import images
# Create your views here.

def home(request):

    print(data)
    context = {'data':data}
    return render(request,"index.html",context)

def collections(request):
    data = images.objects.all()
    context = {'images':data}
    return render(request,'wishes.html',context)