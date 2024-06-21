from django import forms
from .models import Company, Person

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'description', 'location']

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['ism', 'familya', 'lavozim', 'tel', 'image_url']



from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['description']



