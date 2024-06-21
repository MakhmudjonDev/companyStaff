from rest_framework import serializers
from .models import *

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('ism' , 'yosh' , 'tel' , 'lavozim' , 'familya' , "id")


