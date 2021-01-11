from django.contrib import admin
from .forms import MusicForm, UserMusicForm
from .models import Music, Comment, MusicTag, UserUpload


class MusicCreateAdmin(admin.ModelAdmin):
    list_display = ['artist', 'title', 'uploaded_date', 'page_views']
    form = MusicForm
    list_filter = ['artist']
    search_fields = ['artist', 'title']


class UserMusicCreateAdmin(admin.ModelAdmin):
    list_display = ['artist', 'title', 'uploaded_date', 'page_views']
    form = UserMusicForm
    list_filter = ['artist']
    search_fields = ['artist', 'title']


admin.site.register(Music, MusicCreateAdmin)
admin.site.register(Comment)
admin.site.register(MusicTag)
admin.site.register(UserUpload, UserMusicCreateAdmin)
