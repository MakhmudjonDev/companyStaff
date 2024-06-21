from .models import *
from .serializer import DataSerializer
from rest_framework.response import *
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




def dashboard_view(request):
    company = Company.objects.first()

    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CompanyForm(instance=company)

    return render(request, 'dashboard.html', {'form': form})









def home_view(request):
    company = Company.objects.first()
    persons = Person.objects.all()
    return render(request, 'home.html', {
        'company': company,
        'persons': persons,
    })


# @api_view(["GET"])
# def persons(request):
#     all_news = Person.objects.all()
#     all_news_json = DataSerializer(all_news , many=True)
#     return Response(all_news_json.data)
#




# @api_view(["DELETE"])
# def delete_a(request):
#     data = request.data
#     name = data.get("ism")
#     person = Person.objects.get(ism=name)
#     person.delete()
#     return Response({"message" : "Deleted Successfully"} , status=200)



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Company, Person
from .forms import CompanyForm, PersonForm

@login_required
def dashboard_view(request):
    company, created = Company.objects.get_or_create(id=1)
    if request.method == 'POST':
        company_form = CompanyForm(request.POST, instance=company)
        if company_form.is_valid():
            company_form.save()
            return redirect('dashboard')
    else:
        company_form = CompanyForm(instance=company)

    persons = Person.objects.all()
    person_form = PersonForm()
    if request.method == 'POST' and 'person_form' in request.POST:
        person_form = PersonForm(request.POST)
        if person_form.is_valid():
            person_form.save()
            return redirect('dashboard')

    return render(request, 'dashboard.html', {
        'company_form': company_form,
        'company': company,
        'persons': persons,
        'person_form': person_form,
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
