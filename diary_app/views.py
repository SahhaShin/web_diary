from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Count, Avg, Sum


from .models import Diary,Yearly,Monthly

from django.utils import timezone

# Create your views here.

def index(request):
    return render(request,'index.html')

def yearly(request):
    if Yearly.objects is not None:
        content=Yearly.objects
        year=2021

        q = Yearly.objects.annotate(num=Count('id'))
        q_2 = Yearly.objects.annotate(num=Count('box2'))
        count=0
        for i in q:
            count=count+1
        
        count_2=0
        for j in q_2:
            if j.box2==1:
                count_2=count_2+1

        count=count_2/count*100
        
        
        return render(request,'yearly.html',{'check':content, 'count':count, 'n' : range(1), 'year':year})
    else:
        return render(request,'yearly.html')
   

def monthly(request):
    if Monthly.objects is not None:
        month=1
        content=Monthly.objects
        q = Monthly.objects.annotate(num=Count('id'))
        count=0
        for i in q:
            count=count+1
        q_2 = Monthly.objects.annotate(num=Count('box3'))

        count_2=0
        for j in q_2:
            if j.box3==1:
                count_2=count_2+1

        count=count_2/count*100
        
        return render(request,'monthly.html',{'check':content, 'count':count, 'n' : range(1), 'month':month})
    else:
        return render(request,'monthly.html')
 

def write(request):
    return render(request, 'write_diary.html')

def list(request):
    month=1
    if Diary.objects is not None:
        content=Diary.objects
        q = Diary.objects.annotate(num=Count('id'))
        count=0
        for i in q:
            count=count+1
        count=count/31*100

        return render(request,'list_diary.html',{'check':content, 'count':count, 'n' : range(1) , 'month':month})
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
    monthly_save=Monthly()
    
    monthly_save.title3=request.GET['title3']

    monthly_save.save()

    return redirect('../monthly')

def read(request,id):
    content=get_object_or_404(Diary,pk=id)
    return render(request,'read_diary.html',{'check':content})



# 년도 조정
def read_y_next(request,year):
    content=Yearly.objects
    year=year+1
    q = Yearly.objects.annotate(num=Count('id'))
    q_1=0 #년도별 계획수
    q_2 = 0 #계획 완료 수

    #년도별 계획 수 계산
    for num in q: 
        if(num.year1 == year):
            q_1=q_1+1
        # 완료된 계획 수
            if(num.box2 == 1):
                q_2=q_2+1
        else:
            continue
    count=0

    if(q_1==0):
        count=0
    else:   
        count=q_2/q_1*100
    return render(request,'yearly.html',{'check':content, 'year':year , 'n' : range(1), 'count':count})



def read_y_prev(request,year):
    content=Yearly.objects
    year=year-1
    q = Yearly.objects.annotate(num=Count('id'))
    q_1=0 #년도별 계획수
    q_2 = 0 #계획 완료 수

    #년도별 계획 수 계산
    for num in q: 
        if(num.year1 == year):
            q_1=q_1+1
        # 완료된 계획 수
            if(num.box2 == 1):
                q_2=q_2+1
        else:
            continue
    count=0

    if(q_1==0):
        count=0
    else:   
        count=q_2/q_1*100
    return render(request,'yearly.html',{'check':content, 'year':year , 'n' : range(1),'n_2' : range(12), 'count':count})


#  달 조정
def read_m_next(request,month):
    content=Monthly.objects
    month=month+1
    q = Monthly.objects.annotate(num=Count('id'))
    q_1=0 #달 별 계획수
    q_2 = 0 #계획 완료 수

    #달 별 계획 수 계산
    for num in q: 
        if(num.month2 == month):
            q_1=q_1+1
        # 완료된 계획 수
            if(num.box3 == 1):
                q_2=q_2+1
        else:
            continue
    count=0

    if(q_1==0):
        count=0
    else:   
        count=q_2/q_1*100
    return render(request,'monthly.html',{'check':content, 'month':month , 'n' : range(1),'n_2' : range(12), 'count':count})



def read_m_prev(request,month):
    content=Monthly.objects
    month=month-1
    q = Monthly.objects.annotate(num=Count('id'))
    q_1=0 #달 별 계획수
    q_2 = 0 #계획 완료 수

    #달 별 계획 수 계산
    for num in q: 
        if(num.month2 == month):
            q_1=q_1+1
        # 완료된 계획 수
            if(num.box3 == 1):
                q_2=q_2+1
        else:
            continue
    count=0

    if(q_1==0):
        count=0
    else:   
        count=q_2/q_1*100
    return render(request,'monthly.html',{'check':content, 'month':month , 'n' : range(1),'n_2' : range(12), 'count':count})



#  달 조정 - 일기쓰기
def read_d_next(request,month):
    content=Diary.objects
    month=month+1
    q = Diary.objects.annotate(num=Count('id'))
    q_1=0 #달 별 일기 수
   

    #달 별 계획 수 계산
    for num in q: 
        if(num.month1 == month):
            q_1=q_1+1
        
        else:
            continue
    count=0

    if(q_1==0):
        count=0
    else:   
        count=q_1/31*100
    return render(request,'list_diary.html',{'check':content, 'month':month , 'n' : range(1),'n_2' : range(12), 'count':count})



def read_d_prev(request,month):
    content=Diary.objects
    month=month-1
    q = Diary.objects.annotate(num=Count('id'))
    q_1=0 #달 별 일기 수
    

    #달 별 계획 수 계산
    for num in q: 
        if(num.month1 == month):
            q_1=q_1+1
        
        else:
            continue
    count=0

    if(q_1==0):
        count=0
    else:   
        count=q_1/31*100
    return render(request,'list_diary.html',{'check':content, 'month':month , 'n' : range(1),'n_2' : range(12), 'count':count})


def add_y(request):
    return render(request,'add_y.html')

def add_m(request):
    return render(request,'add_m.html')
    
   
   