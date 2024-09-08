from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ImageForm, PostForm
# Create your views here.

@login_required
def post(request):
    ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=3)
    #'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':
    
        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())
    
    
        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()
    
            for form in formset.cleaned_data:
                #this helps to not crash if the user   
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = Images(post=post_form, image=image)
                    photo.save()
            # use django messages framework
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("/")
        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'FGPH/post.html',
                  {'postForm': postForm, 'formset': formset})

def index(request):
    recipes = Recipe.objects.all()
    regions = Region.objects.all()
    print(regions)
    context = {'recipes': recipes, 'regions': regions}
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

def uploadRecipe(request):
    context = {}
    return render(request, 'FGPH/uploadRecipe.html', context)

def addImage(request):
    context = {}
    return render(request, 'FGPH/addImage.html', context)

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