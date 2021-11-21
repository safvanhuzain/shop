from django.shortcuts import render
# Create your views here.
from .models import place


def home(request):
    obj=place.objects.all()
    return render(request,'index.html',{'results':obj})