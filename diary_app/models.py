from django.db import models

# Create your models here.
class Diary(models.Model):
    title1=models.CharField(max_length=50, blank=False) #제목
    
    content1=models.CharField(max_length=200, blank=False) #내용

    date1=models.DateField(null=False, blank=True) #날짜

    time1=models.TimeField(null=False, blank=True) #시간

class Yearly(models.Model):
    title2=models.CharField(max_length=50, blank=False)#목표


class Monthly(models.Model):
    title3=models.CharField(max_length=50, blank=False)#목표
    