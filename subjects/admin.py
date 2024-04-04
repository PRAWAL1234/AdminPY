from django.contrib import admin
from .models import subjects
# Register your models here.

@admin.register(subjects)

class subjectAdmin(admin.ModelAdmin):
    list_display=('id','subject_name')