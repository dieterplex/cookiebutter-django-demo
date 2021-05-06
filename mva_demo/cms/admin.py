from django.contrib import admin

from .models import Category, Song


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug',
                    'created', 'updated']
    list_filter = ['is_active']
    prepopulated_fields = {'slug': ('title',)}
