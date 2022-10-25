from django.urls import path
from generator import views

urlpatterns = [
    path('', views.home, name='home'),
    path('password-generator/', views.password_generator, name='password-generator'),
    path('password-generator/password/', views.password, name='password'),
    path('password-generator/about/', views.about, name='about'),
]
