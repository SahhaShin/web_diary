from django.contrib import admin
from .models import Diary,Yearly,Monthly
# Register your models here.
admin.site.register(Diary)
admin.site.register(Yearly)
admin.site.register(Monthly)