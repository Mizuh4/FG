import json
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RegisteredUser(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)
	title = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="pfp.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	
	def __str__(self):
	    return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
	CATEGORY = (
            ('Authentic', 'Authentic'),
            ('Signature', 'Signature')
    )

	author = models.ForeignKey(RegisteredUser, null=True, on_delete=models.SET_NULL, related_name='recipes')
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=64, null=True, blank=True)
	category = models.CharField(max_length=64, null=True, choices=CATEGORY)
	tags = models.ManyToManyField(Tag)
	steps = models.JSONField(null=True)
	thumbnail = models.ImageField(default='placeholder.png', null=True, blank=True)

	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

	@property
	def recipeSteps(self):
		return json.loads(self.steps)
	
	@recipeSteps.setter
	def recipeSteps(self, steps):
		self.steps=json.dumps(steps)

class Image(models.Model):
	recipe = models.ForeignKey(Recipe, null=True, on_delete=models.SET_NULL, related_name='images')
	photo = models.ImageField(null=True)

	def __str__(self):
		return self.photo.name

	@property
	def imageURL(self):
		try:
			url = self.photo.url
		except:
			url = ''
		return url


class Cookbook(models.Model):
	cookbookAuthor = models.OneToOneField(RegisteredUser, null=True, on_delete=models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	
	def __str__(self):
		return str(self.id)

class CookbookRecipe(models.Model):
	cookbook = models.ForeignKey(Cookbook, null=True, on_delete=models.SET_NULL, related_name='recipes')
	recipe = models.ForeignKey(Recipe, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return str(self.id)