from django.urls import path
from . import views

app_name = 'video'

urlpatterns = [
    path('', views.videos_list, name='index'),

    path('movies_videos/', views.movies_videos, name='movies_videos'),

    path('music_videos/', views.music_videos, name='music_videos'),
    
    path('<slug:slug>/', views.post_detail, name='detail'),

]