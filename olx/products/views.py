from django.shortcuts import render
from django.http import HttpResponse
from.models import Items
# Create your views here.
def about(request):
    x=Items.objects.all()
    return render(request,'index.html',{'x':x})
def aswin(request):
    return HttpResponse("<h2>This page is owned by Mr.Aswin B</h2>")