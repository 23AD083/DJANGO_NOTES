from django.forms import ModelForm
from .models import *

class ExampleModelForm(ModelForm):
    class Meta:
        model = ExampleModel
        fields = '__all__'
        
       

