from ast import mod
from distutils.command import upload
from sre_parse import Verbose
from turtle import mode
from zoneinfo import available_timezones
from django.db import models

# Create your models here.
class Category(models.Model):
    isim = models.CharField(max_length=50,null=True)
    slug = models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
     return self.isim

class Tag(models.Model):
    isim = models.CharField(max_length=50,null=True)
    slug = models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
     return self.isim

class Urunler(models.Model):
 urun_adı = models.CharField(max_length=200,verbose_name="Ürün Adı",help_text="Ürün Adını Giriniz")
 category = models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)
 tags = models.ManyToManyField(Tag,blank=True,null=True)
 aciklama = models.TextField(blank=True,null=True)
 resim = models.ImageField(upload_to="urunler/%Y/%m/%d")
 resimm_uc= models.ImageField(upload_to="urunler/%Y/%m/%d")
 resim_bir = models.ImageField(upload_to="urunler/%Y/%m/%d")
 resim_iki = models.ImageField(upload_to="urunler/%Y/%m/%d")
 tarih = models.DateField(auto_now=True)
 fiyat = models.CharField(max_length=200)
 indirimli_fiyat = models.CharField(max_length=200)
 available =models.BooleanField(default=True)
 facebook = models.URLField(max_length=100,blank=True)
 twitter = models.URLField(max_length=100,blank=True)
 youtube = models.URLField(max_length=100,blank=True)

 def __str__(self):
     return self.urun_adı