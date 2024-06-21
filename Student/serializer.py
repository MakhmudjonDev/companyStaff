
from rest_framework import serializers
from .models import *

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('ism' , 'yosh' , 'sinf' , 'adress' , 'familya')