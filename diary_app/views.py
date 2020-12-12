from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Count


from .models import Diary,Yearly,Monthly

from django.utils import timezone

# Create your views here.

def index(request):
    return render(request,'index.html')

def yearly(request):
    if Yearly.objects is not None:
        content=Yearly.objects
        q = Yearly.objects.annotate(num=Count('id'))
        if q[0].num != 0:
            count=q[0].num / 31
        else:
            count=0
        
        return render(request,'yearly.html',{'check':content, 'count':count})
    else:
        return render(request,'yearly.html')
   

def monthly(request):
    if Monthly.objects is not None:
        content=Monthly.objects
        q = Monthly.objects.annotate(num=Count('id'))
        count=q[0].num / 31
        
        return render(request,'monthly.html',{'check':content, 'count':count})
    else:
        return render(request,'monthly.html')
 

def write(request):
    return render(request, 'write_diary.html')

def list(request):
    if Diary.objects is not None:
        content=Diary.objects
        q = Diary.objects.annotate(num=Count('id'))
        count=q[0].num / 31
        
        return render(request,'list_diary.html',{'check':content, 'count':count})
    else:
        return render(request,'list_diary.html')
    

def storage(request):
    diary_save=Diary()
    
    diary_save.title1=request.GET['title1']

    diary_save.content1=request.GET['content1']

    diary_save.date1=request.GET['date1']

    diary_save.time1=request.GET['time1']
    
    diary_save.save()

    return redirect('../list')

def read(request,id):
    content=get_object_or_404(Diary,pk=id)
    return render(request,'read_diary.html',{'check':content})
   
   