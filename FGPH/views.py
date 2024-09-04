from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'FGPH/home.html', context)

def cookbook(request):
    if request.user.is_authenticated:
        cookbookAuthor = request.user.registereduser
        cookbook, created = Cookbook.objects.get_or_create(cookbookAuthor=cookbookAuthor)
        cookbookRecipes = cookbook.recipes.all()
    else:
        cookbookRecipes = []

    context = {'cookbookRecipes': cookbookRecipes}
    return render(request, 'FGPH/cookbook.html', context)

def updateCookbook(request):
    data = json.loads(request.body)
    recipeId = data['recipeId']
    action = data['action']

    print(f'action: {action}')
    print(f'recipeId: {recipeId}')

    cookbookAuthor = request.user.registereduser
    recipe = Recipe.objects.get(id=recipeId)

    cookbook, created = Cookbook.objects.get_or_create(cookbookAuthor=cookbookAuthor)
    cookbookRecipe, created = CookbookRecipe.objects.get_or_create(cookbook=cookbook, recipe=recipe)
    print(cookbookRecipe)
        
    if action == 'add':
        cookbookRecipe.save()
    elif action == 'remove':
        cookbookRecipe.delete()
    
    return JsonResponse('Cookbook has been updated', safe=False)

def recipe(request, recipeId):
    recipe = Recipe.objects.get(id=recipeId)

    context = {'recipe': recipe}
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