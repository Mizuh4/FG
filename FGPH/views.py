from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .models import *

from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import *

# Create your views here.

def step(request):
    if request == 'POST':
        data = request.POST
        

        return redirect('FGPH:upload')

@login_required
def upload(request):
    categories = Category.objects.all()
    regions = Region.objects.all().values().order_by('name')


    if request.method == 'POST':
        data = request.POST
        thumbnail = request.FILES.get('thumbnail')
        images = request.FILES.getlist('images')

        '''print('data:', data)
        print('category ID:', data['category'])'''
        print('thumbnail:', thumbnail)
        print('images:', images)
        
        category = Category.objects.get(id=data['category'])
        region = Region.objects.get(id=data['region'])


        if data['tag'] != '':
            tag, created = Tag.objects.get_or_create(name=data['tag'])
        else:
            tag = None
        recipe = Recipe.objects.create(
            author=request.user.registereduser,
            name=data['name'],
            category=category,
            region=region,
            description=data['description'],
        )
        if thumbnail:
            Recipe.objects.filter(id=recipe.id).update(thumbnail=thumbnail)

        recipe.tags.add(tag)

        for image in images:
            Image.objects.create(
                recipe=recipe,
                photo=image
            )

        cookbookAuthor = request.user.registereduser
        recipe = Recipe.objects.get(id=recipe.id)
        print('recipe id', recipe.id)

        cookbook, created = Cookbook.objects.get_or_create(cookbookAuthor=cookbookAuthor)
        CookbookRecipe.objects.get_or_create(cookbook=cookbook, recipe=recipe)
        return redirect('FGPH:cookbook')

    context = {'categories': categories, 'regions': regions}
    return render(request, 'FGPH/upload.html', context)

def index(request):
    category = request.GET.get('category')
    region = request.GET.get('region')

    if category:
        recipes = Recipe.objects.filter(category__name__contains=category)
    elif region:
        recipes = Recipe.objects.filter(region__name__contains=region)
    else:
        recipes = Recipe.objects.all()

    categories = Category.objects.all()
    regions = Region.objects.all().values().order_by('order')
    #print(regions)
    context = {'recipes': recipes, 'regions': regions, 'categories': categories}
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

def recipe(request, recipeId):
    recipe = Recipe.objects.get(id=recipeId)
    images = recipe.images.all()

    context = {'recipe': recipe, 'images': images}
    return render(request, 'FGPH/recipe.html', context)

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

'''def addImage(request):
    context = {}
    return render(request, 'FGPH/addImage.html', context)'''

def profile(request):
    user = request.user
    #group = list(user.groups.values_list('name', flat = True))


    context = {'user': user}
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