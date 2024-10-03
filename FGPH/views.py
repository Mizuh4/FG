from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

from django.urls import reverse

from FGPH.decorators import unauthenticated_user
from .models import *

from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from .forms import *

# Create your views here.
def index(request):
    categories = Category.objects.all()
    regions = Region.objects.all().values().order_by('order')

    cookbookAuthor = request.user.registereduser
    cookbook = Cookbook.objects.get(cookbookAuthor=cookbookAuthor)
    pks = cookbook.recipes.values_list('recipe')
    cookbookrecipes = Recipe.objects.filter(id__in=pks)
    print(cookbookrecipes)

    category = request.GET.get('category')
    region = request.GET.get('region')
    query = request.GET.get("q")
    
    if category:
        recipes = Recipe.objects.filter(category__name__contains=category)
    elif region:
        recipes = Recipe.objects.filter(region__name__contains=region)
    elif query:
        recipes = Recipe.objects.filter(
            Q(name__icontains=query) | Q(tags__name__icontains=query) | Q(author__name__icontains=query) |
            Q(ingredients__icontains=query)
        ).distinct()
    else:
        recipes = Recipe.objects.all()

    #print(regions)
    context = {'recipes': recipes, 'regions': regions, 'categories': categories,
               'cookbookrecipes': cookbookrecipes}
    return render(request, 'FGPH/home.html', context)


@login_required(login_url='FGPH:login')
def cookbook(request):
    categories = Category.objects.all()
    if request.user.is_authenticated:
        cookbookAuthor = request.user.registereduser
        cookbook, created = Cookbook.objects.get_or_create(cookbookAuthor=cookbookAuthor)
        cookbookRecipes = cookbook.recipes.all()
    else:
        cookbookRecipes = []

    context = {'cookbookRecipes': cookbookRecipes, 'categories': categories}
    return render(request, 'FGPH/cookbook.html', context)

def recipe(request, recipeId):
    categories = Category.objects.all()
    recipe = Recipe.objects.get(id=recipeId)
    images = recipe.images.all()
    print(images.order_by("id"))
    steps = recipe.steps
    ingredients = recipe.ingredients

    context = {'categories': categories, 'recipe': recipe, 'images': images, 'steps': steps, 'ingredients': ingredients}
    return render(request, 'FGPH/recipe.html', context)

@login_required(login_url='FGPH:login')
def updateCookbook(request):
    data = json.loads(request.body)
    recipeId = data['recipeId']
    action = data['action']

    '''print(f'action: {action}')
    print(f'recipeId: {recipeId}')'''

    cookbookAuthor = request.user.registereduser
    recipe = Recipe.objects.get(id=recipeId)

    cookbook, created = Cookbook.objects.get_or_create(cookbookAuthor=cookbookAuthor)
    cookbookRecipe, created = CookbookRecipe.objects.get_or_create(cookbook=cookbook, recipe=recipe)
    #print(cookbookRecipe)
        
    if action == 'add':
        cookbookRecipe.save()
    elif action == 'remove':
        cookbookRecipe.delete()
    
    return JsonResponse('Cookbook has been updated', safe=False)

@login_required(login_url='FGPH:login')
def uploadRecipe(request, *args):
    categories = Category.objects.all()
    regions = Region.objects.all().order_by('name')

    if request.method == 'POST':
        data = request.POST
        thumbnail = request.FILES.get('thumbnail')
        images = request.FILES.getlist('images')
        tags = data.getlist('tag')
        steps = data.getlist('step')
        ingredients = data.getlist('ingredient')
        #serving_size = data.get('serving_size')

        category = Category.objects.get(id=data['category'])
        region = Region.objects.get(id=data['region'])
        
        if args:
            for arg in args:
                recipeId = arg
        else:
            recipeId = None

        '''
        print('desc:', data['description'])
        print('thumbnail:', type(thumbnail))
        print('tags:', data.getlist('tag'))
        print('tags:', data['tag'])
        print('category ID:', data['category'])
        print('images:', images)
        '''

        recipe, created = Recipe.objects.update_or_create(
            id=recipeId,
            defaults={
                'author': request.user.registereduser,
                'name': data['name'],
                'category': category,
                'region': region,
                'description': data['description'],
                'steps': steps,
                'ingredients': ingredients,
                'preparation_time': data['preparation_time'],
                'serving_size': data['serving_size'],
                }
        )

        '''recipe, created = Recipe.objects.get_or_create(
            author=request.user.registereduser,
            name=data['name'],
            category=category,
            region=region,
            description=data['description'],
            steps=steps,
            ingredients=ingredients
        )'''

        '''if serving_size:
            recipe.serving_size = serving_size
            recipe.save()'''

        if tags:
            recipe.tags.clear()
            for tag in tags:
                if tag:
                    print(tag)
                    print(type(tag))
                    tag, created = Tag.objects.get_or_create(name__iexact=tag, defaults={'name': tag})
                    print(tag)
                    print(type(tag))
                    print(created)
                    recipe.tags.add(tag)
        
        if thumbnail:
            recipe.thumbnail = thumbnail
            recipe.save()
            #print('Thumbnail updated')
        
        if images:
            Image.objects.filter(recipe=recipe).delete()
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

@login_required(login_url='FGPH:login')
def editRecipe(request, recipeId):
    recipe = Recipe.objects.get(id=recipeId)
    categories = Category.objects.all()
    regions = Region.objects.all().order_by('name')
    tags = recipe.tags.values_list()

    '''print(recipe.tags.values())
    print('desc:', type(recipe.description))'''

    if request.method == 'POST':
        uploadRecipe(request, recipeId)
        # return HttpResponseRedirect(reverse('FGPH:recipe', args=[recipeId]))
        return redirect('FGPH:cookbook')
    
    context = {'recipe': recipe, 'tags': tags, 'categories': categories, 'regions': regions}
    return render(request, 'FGPH/upload.html', context)

@login_required
def deleteRecipe(request, recipeId):
    recipe = Recipe.objects.get(id=recipeId)
    recipe.delete()
    return redirect('FGPH:cookbook')

@login_required(login_url='FGPH:login')
def profile(request):
    categories = Category.objects.all()
    user = request.user
    if request.method == 'POST':
        data = request.POST
        username = request.user.username
        password = data.get('password')

        if authenticate(request, username=username, password=password) is not None:
            print(user.registereduser.name)
            print(user.registereduser.title)
            user.username = data['username']
            user.email = data['email']
            user.registereduser.name = data['name']
            user.registereduser.title = data['title']
            print(user.registereduser.name)
            print(user.registereduser.title)
            try:
                user.save()
                user.registereduser.save()
                messages.success(request, 'Profile has been updated.')
            except IntegrityError:
                messages.info(request, 'Username already exists.')
                
        else:
            messages.info(request, 'Password is incorrect.')
            print('Password is incorrect.')

    #group = list(user.groups.values_list('name', flat = True))

    context = {'user': user, 'categories': categories}
    return render(request, 'FGPH/profile.html', context)


@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            '''group = Group.objects.get(name='user')
            user.groups.add(group)
            RegisteredUser.objects.create(
                user=user,
            )'''

            messages.success(request, f'Account was created for {username}')
            return HttpResponseRedirect(reverse('FGPH:login'))

    context = {'form': form}
    return render(request, 'FGPH/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('FGPH:home'))
        else:
            messages.info(request, 'Username OR Password is incorrect.')

    context = {}
    return render(request, 'FGPH/login.html', context)

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse('FGPH:home'))