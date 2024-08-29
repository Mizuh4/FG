from django.urls import path
from . import views

app_name = 'FGPH'
urlpatterns = {
    path("", views.index, name='index'),
    path("cookbooks/", views.cookbooks, name='cookbooks'),
    path("recipe/", views.recipe, name='recipe'),

    path("login/", views.login, name='login'),
    path("logout/", views.logout, name='logout'),
    path("signup/", views.signup, name='section')
}