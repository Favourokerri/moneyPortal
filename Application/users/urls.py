from django.urls import path, include
from .views import SignUp, Login, Logout

urlpatterns = [
    path('', SignUp, name='signUp'),
    path('login', Login, name='login'),
    path('logout', Logout, name='logout')
     
]
