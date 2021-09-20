from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html')

def login(request):
    return render(request, 'recipes/login.html')

def register(request):
    return render(request, 'recipes/register.html')