from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'FGPH/home.html', context)


def cookbook(request):
    if request.user.is_authenticated:
        author = request.user.registereduser
        cookbook = author.recipes.all()
        recipecount = cookbook.count()
    else:
        cookbook = []
        recipecount = 0

    context = {'cookbook': cookbook, 'recipecount': recipecount}
    return render(request, 'FGPH/cookbook.html', context)

def recipe(request):
    context = {}
    return render(request, 'FGPH/recipe.html', context)

def profile(request):
    context = {}
    return render(request, 'FGPH/profile.html', context)

def addToCookbook(request):
    return JsonResponse('Recipe was added to cookbook', safe=False)

def login(request):
    context = {}
    return render(request, 'FGPH/home.html', context)

def logout(request):
    context = {}
    return render(request, 'FGPH/home.html', context)

def signup(request):
    context = {}
    return render(request, 'FGPH/home.html', context)