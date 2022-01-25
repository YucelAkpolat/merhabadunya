from re import template
from django.shortcuts import render
from django.views.generic import TemplateView
from pages.models import Contact
from urunler.models import Urunler
from blog.models import Post,Video
from django.views.generic.edit import FormView
from  pages.forms import ContactForm
from django.core.mail import send_mail
# Create your views here.
#def index(request):
   # return render(request,'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['urunler'] = Urunler.objects.filter(available=True).order_by('-id')[:4]
        context['posts'] = Post.objects.filter(available=True).order_by('-id')[:3]
        context['iframes'] = Video.objects.filter(available=True).order_by('-id')[:1]

        return context

class AboutView(TemplateView):
 template_name = 'about.html'

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'iletisim.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'iletisim.html', context)