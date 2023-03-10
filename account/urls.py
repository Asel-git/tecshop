from . import views
from django.contrib import admin
from django.urls import path
# from django.contrib.auth import views as auth_views
from account import views as user_views
from .views import login



urlpatterns = [
    path('register/', user_views.register, name='register'),

    path('login/', login, name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
]


    
