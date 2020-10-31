from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('advertise/', views.advertise, name='advertise'),
    path('about-us/', views.about, name='about-us'),
    path('promote/', views.promote, name='promote'),
    path('privacy-policy/', views.privacy, name='privacy-policy'),
    path('s/', views.search, name='search')
]
