from django.contrib import admin


from .models import Video, Comment, VidTags

admin.site.register(Video)
admin.site.register(VidTags)
admin.site.register(Comment)
