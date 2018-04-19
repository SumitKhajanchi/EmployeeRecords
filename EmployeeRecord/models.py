from django.db import models
from django.utils import timezone

class Post(models.Model):
    employee_id = models.IntegerField()
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    experience = models.TextField()
    joining_date = models.DateField()

    def __str__(self):
        return self.name
    

# Create your models here.
