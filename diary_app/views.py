from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def yearly(request):
    return render(request, 'yearly.html')

def monthly(request):
    return render(request, 'monthly.html')