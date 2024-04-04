from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class News(models.Model):
    news_title=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blog=models.TextField()
    image=models.ImageField(upload_to='news')
    created_date=models.DateTimeField(auto_now_add=True)
