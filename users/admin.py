from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['phone','login']
    ordering = ['login']
    search_fields = ['age']


@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'tarif', 'date_time']
    ordering = ['user', 'date_time']
    search_fields = ['user', 'tarif']


@admin.register(Tarifs)
class TarifAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['price']
    search_fields = ['name']


@admin.register(UsedFilms)
class UsedFilmAdmin(admin.ModelAdmin):
    list_display = ['user', 'film', 'status']
    ordering = ['user', 'datetime']
    search_fields = ['user', 'film', 'datetime']