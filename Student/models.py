from django.db import models

class Student(models.Model):
    ism = models.CharField(max_length=45)
    familya = models.CharField(max_length=45)
    adress = models.CharField(max_length=45)
    yosh = models.IntegerField()
    sinf = models.IntegerField()