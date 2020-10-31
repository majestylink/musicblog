from django.contrib import admin


from .models import Poem, Comment


admin.site.register(Poem)
admin.site.register(Comment)

