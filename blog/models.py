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

class Post(models.Model):
 isim = models.CharField(max_length=200)
 category = models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)
 tags = models.ManyToManyField(Tag,blank=True,null=True)
 aciklama = models.TextField(blank=True,null=True)
 resim = models.ImageField(upload_to="post/%Y/%m/%d",null=True)
 vıdeo =  models.CharField(max_length=2000)
 tarih = models.DateField(auto_now=True)
 available =models.BooleanField(default=True)
 
 

 def __str__(self):
     return self.isim


class Video(models.Model):
    iframe =  models.CharField(max_length=2000,blank=True)
    available =models.BooleanField(default=True)
    tarih = models.DateField(auto_now=True)