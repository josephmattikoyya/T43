from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def page2(request):
    return render(request, 'page2.html')

def page3(request):
    return render(request, 'page3.html')