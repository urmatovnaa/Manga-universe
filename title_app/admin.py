from django.contrib import admin

from title_app.models import Title, Tag, Genre

admin.site.register(Tag)
admin.site.register(Genre)
admin.site.register(Title)
