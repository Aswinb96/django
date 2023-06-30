from django.shortcuts import render
from django.http import HttpResponse
from.models import Items
# Create your views here.
def home(request):
    x=Items.objects.all
    return render(request,'index.html',{'x':x})
def aswin(request):
    return HttpResponse("<p>This is my first Django project</p>")
