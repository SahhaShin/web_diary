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
        a = Yearly.objects.annotate(num=Count('id'))
        
        count= 0 / 31
        
        
        return render(request,'yearly.html',{'check':content, 'count':count, 'n' : range(1)})
    else:
        return render(request,'yearly.html')
   

def monthly(request):
    if Monthly.objects is not None:
        content=Monthly.objects
        q = Monthly.objects.annotate(num=Count('id'))
        count=0 / 31
        
        return render(request,'monthly.html',{'check':content, 'count':count, 'n' : range(1)})
    else:
        return render(request,'monthly.html')
 

def write(request):
    return render(request, 'write_diary.html')

def list(request):
    if Diary.objects is not None:
        content=Diary.objects
        q = Diary.objects.annotate(num=Count('id'))
        count=q[0].num / 31
       
        return render(request,'list_diary.html',{'check':content, 'count':count, 'n' : range(1)})
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

def storage_y(request):
    yearly_save=Yearly()
    
    yearly_save.title2=request.GET['title2']

    yearly_save.box2=0
  
    yearly_save.save()

    return redirect('../yearly')

# 체크박스 상태 변화
def storage_yc(request, id):
    content=get_object_or_404(Yearly,pk=id)
    if content.box == 0:
        content.box2 = 1
    else:
        content.box2 = 0
    return redirect('../yearly')



def storage_m(request):
    monthly_save=Diary()
    
    monthly_save.title3=request.GET['title3']

    monthly_save.save()

    return redirect('../monthly')

def read(request,id):
    content=get_object_or_404(Diary,pk=id)
    return render(request,'read_diary.html',{'check':content})

def add(request):
    return render(request,'add.html')
    
   
   