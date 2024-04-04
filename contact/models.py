from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.IntegerField()
    messages=models.TextField()
    

