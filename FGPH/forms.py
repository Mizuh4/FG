from django import forms
from .models import *

class PostForm(forms.ModelForm):
    '''title = forms.CharField(max_length=128)
    body = forms.CharField(max_length=245, label="Item Description.")'''
 
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'category', 'tags', 'steps', 'thumbnail']
 

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = Images
        fields = ('photo', )

'''class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        thumbnail = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        fields = ['name', 'description', 'category', 'tags', 'steps', 'thumbnail']'''