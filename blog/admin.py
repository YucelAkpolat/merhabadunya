from django import views
from django.contrib import admin
from django.contrib import admin
from . models import Post,Video
from . models import Category
from . models import Tag

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
 list_display = ('isim',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('isim',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('isim',)}

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('iframe',)
