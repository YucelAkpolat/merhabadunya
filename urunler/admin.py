from django.contrib import admin
from . models import Urunler
from . models import Category
from . models import Tag

# Register your models here.

@admin.register(Urunler)
class UrunlerAdmin(admin.ModelAdmin):
 list_display = ('urun_adı',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('isim',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('isim',)}
