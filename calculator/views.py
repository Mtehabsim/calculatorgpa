from django.shortcuts import render
from django.views.generic import ListView
from .models import Materials
#def home(request):
#   return render(request,'calculator/home.html',{})

class HomeView(ListView):
    model = Materials
    template_name = 'calculator/home.html'

class AddView(ListView):
    model = Materials
    template_name = 'calculator/add.html'
    fields = '__all__'