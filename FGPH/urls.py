from django.urls import path
from . import views

app_name = 'FGPH'
urlpatterns = [
    path("", views.index, name='home'),
    path("cookbook/", views.cookbook, name='cookbook'),
    path("recipe/<str:recipeId>", views.recipe, name='recipe'),

    path("update_cookbook/", views.updateCookbook, name='update_cookbook'),
    path("post/", views.post, name='post'),

    path("profile/", views.profile, name='profile'),
    path("login/", views.login, name='login'),
    path("logout/", views.logout, name='logout'),
    path("signup/", views.signup, name='section')
]