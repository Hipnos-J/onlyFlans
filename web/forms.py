from django import forms
from .models import ContactForm

# Create your forms here.

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email','customer_name',  'message']
        