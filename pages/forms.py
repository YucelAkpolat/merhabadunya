import email
from email import message
from django import forms
from . models import Contact


class ContactForm(forms.ModelForm):
    subject = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()


    class Meta:
        model = Contact
        fields = ['subject','email','message']