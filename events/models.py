from django.db import models

# Create your models here.
class Events(models.Model):
    events_name=models.CharField(max_length=200)
    about=models.TextField()
    created_date=models.DateField(auto_now_add=True)
    created_time=models.DateTimeField(auto_now_add=True)
    location=models.CharField(max_length=500)
    