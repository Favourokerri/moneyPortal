from django.urls import path
from . import views

urlpatterns = [
    path('sigup', views.signup, name='sigup'),
    path('login', views.login, name='login'),
    path('text_token', views.text_token, name='text_token'),
]
