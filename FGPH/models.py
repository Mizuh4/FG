import json
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

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
    
class Region(models.Model):
	name = models.CharField(max_length=64, null=True)
	alias = models.CharField(max_length=64, null=True, blank=True)
	order = models.FloatField(null=True, blank=True)

	def __str__(self):
		return self.name

class Tag(models.Model):
    name = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"

class Recipe(models.Model):
	author = models.ForeignKey(RegisteredUser, null=True, on_delete=models.CASCADE, related_name='recipes')
	name = models.CharField(max_length=64)
	category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, related_name='recipes')
	tags = models.ManyToManyField(Tag)
	thumbnail = models.ImageField(default='placeholder.png')
	region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.SET_NULL, related_name='recipes')
	description = models.CharField(max_length=200, null=True, blank=True)
	steps = models.JSONField(null=True)
	ingredients = models.JSONField(null=True)
	preparation_time = models.CharField(max_length=64, null=True, blank=True)
	serving_size = models.IntegerField(
		null=True,
		blank=True,
        validators=[
            MaxValueValidator(500),
            MinValueValidator(1)
        ]
    )

	date_created = models.DateTimeField(auto_now_add=True, null=True)
	date_modified = models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		return self.name
	
	@property
	def index(self):
		return self.index()

	@property
	def recipeSteps(self):
		return json.loads(self.steps)
	
	@recipeSteps.setter
	def recipeSteps(self, steps):
		self.steps=json.dumps(steps)

def get_image_filename(instance, filename):
    title = instance.recipe.name
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)  

class Image(models.Model):
	recipe = models.ForeignKey(Recipe, null=True, on_delete=models.CASCADE, related_name='images')
	photo = models.ImageField(null=True, upload_to=get_image_filename, verbose_name='Image')

	def __str__(self):
		return str(self.recipe.name)

	@property
	def imageURL(self):
		try:
			url = self.photo.url
		except:
			url = ''
		return url

class Cookbook(models.Model):
	cookbookAuthor = models.OneToOneField(RegisteredUser, null=True, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	
	def __str__(self):
		return str(self.cookbookAuthor.name)

class CookbookRecipe(models.Model):
	cookbook = models.ForeignKey(Cookbook, null=True, on_delete=models.CASCADE, related_name='recipes')
	recipe = models.ForeignKey(Recipe, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.cookbook.cookbookAuthor.name)