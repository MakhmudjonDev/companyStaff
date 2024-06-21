from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Person(models.Model):
    ism = models.CharField(max_length=50)
    familya = models.CharField(max_length=50)
    lavozim = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    image_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.ism} {self.familya}'
