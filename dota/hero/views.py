# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
    
def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about_team.html')

def contact(request):
    return render(request, 'contact.html')
