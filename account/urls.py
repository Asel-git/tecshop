from django.urls import path
from .views import user_login

urlpatterns = [
    # post views
    path('', user_login, name='login'),
]