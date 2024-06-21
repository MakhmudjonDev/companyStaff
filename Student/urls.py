from django.urls import path , include
from .views import *

urlpatterns = [
    path('student/home/' , bosh_ekran),
    path('student/add/' , qoshish),
    path('student/update/' , tahrirlash),
    path('student/delete/' , ochirish),
    path('student/get/' , student_get),
    # path('del/' , student_delete),
    # path('post/' , student_post)

]