from unicodedata import category
from zoneinfo import available_timezones
from django.shortcuts import render
from django.template import context
from . models import Category, Urunler,Tag
from blog.models import Post
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.
"""def urunler(request):

    urunler = Urunler.objects.all().order_by('-id')
    posts = Post.objects.all().order_by('-id')
    categories = Category.objects.all().order_by('-id')
    tags = Tag.objects.all().order_by('-id')

    context = {
        'urunler':urunler,
        'posts':posts,
        'categories':categories,
        'tags':tags
    }
    return render(request,'urunler.html',context)"""

def urunler(request, category_slug=None,tag_slug=None):
    Category_page = None
    tag_page = None
    urunler = Urunler.objects.all().order_by('-id')
    posts = Post.objects.all().order_by('-id')
    categories = Category.objects.all().order_by('-id')
    tags = Tag.objects.all().order_by('-id')

     
    if category_slug != None:
         category_page = get_object_or_404(Category, slug= category_slug)
         urunler = Urunler.objects.filter(available=True,category=category_page)

    elif tag_slug != None:
        tag_page = get_object_or_404(Tag, slug=tag_slug)
        urunler = Urunler.objects.filter(available=True,tags=tag_page)

    else:
      urunler = Urunler.objects.all().order_by('-id')
      posts = Post.objects.all().order_by('-id')
    context = {
        'urunler':urunler,
        'posts':posts,
        'categories':categories,
        'tags':tags
    }
    return render(request,'urunler.html',context)

    



def urun_detay(request,category_slug,urun_id):
    urun = Urunler.objects.get(category__slug=category_slug, id = urun_id)
    
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'urun':urun,
        'tags':tags,
        'categories':categories
    }

    return render(request,'urun_detay.html',context)


def search(request):
    urunler = Urunler.objects.filter(Q(urun_adı__contains=request.GET['search']) | Q(fiyat__contains=request.GET['search']))
    
    posts = Post.objects.all().order_by('-id')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'urunler':urunler,
        'posts':posts,
        'categories':categories,
        'tags':tags
    }
    return render(request,'urunler.html',context)
 













"""def urun_kategory(request,category_slug):
    urunler = Urunler.objects.all().filter(category__slug=category_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'urunler':urunler,
        'tags':tags,
        'categories':categories
    }

    return render(request,'urunler.html',context)"""

"""def tag_kategory(request,tag_slug):
    urunler = Urunler.objects.all().filter(tags__slug=tag_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'urunler':urunler,
        'tags':tags,
        'categories':categories
    }

    return render(request,'urunler.html',context)"""