from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('upload/', views.upload, name='upload'),

    path('<slug:slug>/', views.detail, name='detail'),

]