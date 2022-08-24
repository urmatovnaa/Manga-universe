from django.contrib import admin

from title_app.models import Tag, Genre, AdultContent, TitleStatus, \
    ReleaseFormat, TitleType, TranslatorStatus, Title, Rating


@admin.register(Title)
class CategoryModelAdmin(admin.ModelAdmin):
    readonly_fields = ['title_url', 'date_created']
    list_display = ['english_name']


admin.site.register(Tag)
admin.site.register(Genre)
admin.site.register(AdultContent)
admin.site.register(TitleStatus)
admin.site.register(ReleaseFormat)
admin.site.register(TitleType)
admin.site.register(TranslatorStatus)
admin.site.register(Rating)




