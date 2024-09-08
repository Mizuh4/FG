from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(RegisteredUser)
#admin.site.register(Region)
admin.site.register(Tag)
admin.site.register(Recipe)
admin.site.register(Images)
admin.site.register(Cookbook)
admin.site.register(CookbookRecipe)

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    ordering = ['order']