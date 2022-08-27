from django.contrib import admin

from django.contrib.admin.options import TabularInline

from info_section_app.models import SimilarLike, SimilarDislike, SimilarTitle


class SimilarLikeAdminInLine(TabularInline):
    extra = 1
    model = SimilarLike


class SimilarDislikeAdminInline(TabularInline):
    extra = 1
    model = SimilarDislike


@admin.register(SimilarTitle)
class RestaurantModelAdmin(admin.ModelAdmin):
    inlines = (SimilarDislikeAdminInline, SimilarLikeAdminInLine)

