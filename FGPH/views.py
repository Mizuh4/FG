from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'FGPH/home.html', context)

def cookbook(request):
    context = {}
    return render(request, 'FGPH/cookbook.html', context)

def recipe(request):
    context = {}
    return render(request, 'FGPH/recipe.html', context)

def profile(request):
    context = {}
    return render(request, 'FGPH/profile.html', context)

def login(request):
    context = {}
    return render(request, 'FGPH/home.html', context)

def logout(request):
    context = {}
    return render(request, 'FGPH/home.html', context)

def signup(request):
    context = {}
    return render(request, 'FGPH/home.html', context)