from django.db import models

# Create your models here.

class Teachers(models.Model):
    teacher_name=models.CharField(max_length=200)
    position=models.CharField(max_length=200)
    email=models.EmailField()
    mobile_number=models.IntegerField()

    def __str__(self):
        return self.teacher_name