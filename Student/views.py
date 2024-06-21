from django.shortcuts import render
from .models import *
from .serializer import DataSerializer
from rest_framework.response import *
from rest_framework.decorators import api_view
from rest_framework import *
def bosh_ekran(request):
    student_list = {
        'studentlar' : Student.objects.all(),
    }
    return render(request , 'bosh_ekran.html' , student_list)

def qoshish(request):

    if request.method =='POST':
        name = request.POST['ism']
        age = request.POST['yosh']
        adress = request.POST['adress']
        sinf = request.POST['sinf']
        familya = request.POST['familya']
        oquvchi = Student(ism = name ,adress = adress , sinf = sinf , yosh = age , familya = familya)
        oquvchi.save()
    return render(request , 'qoshish.html')

def tahrirlash(request):
    if request.method == 'POST':
        oquvchi_id = request.POST['id']
        oquvchi = Student.objects.get(id = oquvchi_id)
        oquvchi.ism = request.POST['ism']
        oquvchi.familya = request.POST['familya']
        oquvchi.yosh = request.POST['yosh']
        oquvchi.sinf = request.POST['sinf']
        oquvchi.adress = request.POST['adress']
        oquvchi.save()
    return render(request , 'tahrirlash.html')


def ochirish(request):
    if request.method== 'POST':
        oquvchi_id = request.POST['id']
        oquvchi = Student.objects.get(id = oquvchi_id)
        oquvchi.delete()
    return render(request , 'ochirish.html')

@api_view(['POST'])
def student_post(request):
    new_data = DataSerializer(data = request.data)
    if new_data.is_valid():
        new_data.save()
        return Response(new_data.data)

@api_view(["GET"])
def student_get(request):
    student = Student.objects.all()
    student_json = DataSerializer(student, many=True)
    return Response(student_json.data)

@api_view(["DELETE"])
def student_delete(request):
    student = request.data
    student_id= student.get("id")
    talaba = Student.objects.get(id = student_id)
    talaba.delete()
    return Response({"message " : "Delete successfully"})

@api_view(["PUT"])
def student_update(request):
    student = request.data
    student_id= student.get("id")
    talaba = Student.objects.get(id = student_id)
    talaba.ism = student.get("ism")
    talaba.familya = student.get("familya")
    talaba.adress = student.get("adress")
    talaba.sinf = student.get("sinf")
    talaba.yosh = student.get("yosh")
    return Response({"message " : "Update successfully"})
