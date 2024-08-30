from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RegisteredUser(models.Model):
	ACCESS = (
            ('User', 'User'),
            ('Contributor', 'Contributor')
    )
	
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)
	ACCESS = models.CharField(max_length=64, null=True, choices=ACCESS)
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

	author = models.ForeignKey(RegisteredUser, null=True, on_delete=models.SET_NULL, related_name='author')
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=64, null=True, blank=True)
	category = models.CharField(max_length=64, null=True, choices=CATEGORY)
	tags = models.ManyToManyField(Tag)
	image = models.ImageField(null=True, blank=True)

	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	
class Cookbook(models.Model):
    RegisteredUser = models.ForeignKey(RegisteredUser, null=True, on_delete=models.SET_NULL, related_name='cookbook')
    Recipe = models.ForeignKey(Recipe, null=True, on_delete=models.SET_NULL, related_name='cookbook')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.RegisteredUser.name)