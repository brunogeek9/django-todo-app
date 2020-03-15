from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
def home(request):
    template = loader.get_template('home.html')
    
    #rendering the template in HttpResponse
    return HttpResponse(template.render())