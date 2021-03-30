from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=255)
    roll= models.IntegerField(unique=True)
    city= models.CharField(max_length=255)
    marks= models.FloatField()
    pass_fail=models.BooleanField()
    created= models.DateField(auto_now_add=True)
