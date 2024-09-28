from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = 'FGPH'
urlpatterns = [
    path("", views.index, name='home'),
    path("cookbook/", views.cookbook, name='cookbook'),
    path("recipe/<str:recipeId>", views.recipe, name='recipe'),

    path("update_cookbook/", views.updateCookbook, name='update_cookbook'),
    path("upload_recipe/", views.uploadRecipe, name='uploadRecipe'),
    path("edit_recipe/<str:recipeId>/", views.editRecipe, name='editRecipe'),
    path("delete_recipe/<str:recipeId>/", views.deleteRecipe, name='deleteRecipe'),

    path("profile/", views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(
        success_url=reverse_lazy('FGPH:password_reset_done'), 
        template_name="FGPH/password_reset.html"
        ), name='password_reset'),

    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name="FGPH/password_reset_sent.html"
        ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('FGPH:password_reset_complete'),
        template_name="FGPH/password_reset_form.html"
        ), name='password_reset_confirm'),

    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="FGPH/password_reset_done.html"
        ), name='password_reset_complete'),

]