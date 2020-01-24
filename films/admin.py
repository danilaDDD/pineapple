from django.contrib import admin
from django.forms import Textarea
from .models import *


# Register your models here.
class GenreInlineAdmin(admin.TabularInline):
    model = Film.genres.through
    extra = 1
    list_display = ['name']


class DirectorInlineAdmin(admin.TabularInline):
    model = Film.directors.through
    extra = 1
    list_display = ['first_name', 'second_name']


class ActorInlineAdmin(admin.TabularInline):
    model = Film.actors.through
    extra = 1
    list_display = ['first_name', 'second_name']


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    ordering = ['year']
    search_fields = ['title', 'year']
    list_display = ['title', 'year']

    inlines = (
        GenreInlineAdmin,
        DirectorInlineAdmin,
        ActorInlineAdmin,
    )

    mds.TextField: {'widget': Textarea}
    exclude = ('genres', 'directors', 'actors')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
    list_display = ['name']
    inlines = (
        GenreInlineAdmin,
    )


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    ordering = ['first_name', 'second_name']
    search_fields = ['first_name', 'second_name']
    list_display = ['first_name', 'second_name']


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    ordering = ['first_name', 'second_name']
    search_fields = ['first_name', 'second_name']
    list_display = ['first_name', 'second_name']


