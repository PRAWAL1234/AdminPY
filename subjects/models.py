from django.db import models
from teachers.models import Teachers
# Create your models here.
class subjects(models.Model):
    subject_name=models.CharField(max_length=100)
    description=models.TextField()
    images=models.ImageField(upload_to='subjects')
    teachers=models.ForeignKey(Teachers,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.subject_name