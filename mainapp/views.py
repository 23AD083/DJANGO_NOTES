from urllib import request
from django.shortcuts import redirect, render
from .forms import *
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def mainapp_view(request):
    context ={
    'form': ExampleModelForm(),
    }
    if request.method == 'POST':
         print(request.POST)
         
         form = ExampleModelForm(request.POST)
         if form.is_valid():
             form.save()
             context['form'] = form
             return render(request, 'mainapp.html', context)
    
def mainapp_show(request):
    data = ExampleModel.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'app_show.html', context)

def deleteproduct(request, pk):
    product = ExampleModel.objects.get(id=pk)
    product.delete()
    return redirect('/mainapp/mainapp_show/')

