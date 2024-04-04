from django.contrib import admin
from .models import Contact
# Register your models here.

admin.site.register(Contact)

class contactAdmin(admin.ModelAdmin):
    list_display=('firstname','email','phone')