from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('ceosignup/', views.ceosignup, name='ceosignup'),
    path('logout/', views.logout, name='logout'),
    
]