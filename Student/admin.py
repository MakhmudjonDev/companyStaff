from django.contrib import admin
from .models import *
# Register your models here.

class MemberAdmin (admin.ModelAdmin):
    list_display = ('ism' , 'familya' , 'yosh' , 'sinf' , 'adress')

admin.site.register(Student , MemberAdmin)