from django.contrib import admin
from .models import Teachers
# Register your models here.
@admin.register(Teachers)
class teacher(admin.ModelAdmin):
    list_display=('id','teacher_name','mobile_number')