from django.shortcuts import render, redirect
from .models import Flan
from .forms import ContactFormForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
  flanes_publicos= Flan.objects.filter(is_private=False)
  return render(request, 'index.html', {'flanes': flanes_publicos})


def about(request):
  return render(request, 'about.html')

@login_required
def welcome(request):
  flanes_privados = Flan.objects.filter(is_private=True)
  return render(request, 'welcome.html', {'flanes': flanes_privados})


def contact(request):
  if request.method == 'POST':
    form = ContactFormForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('exito') 
  else:
    form = ContactFormForm()
   
  return render(request, 'contact.html', {'form':form})

def exito(request):
  return render(request, 'exito.html')

def flan_detail(request, flan_id):
    flan = Flan.objects.get(id=flan_id)
    return render(request, 'flan_detail.html', {'flan': flan})

class CustomLoginView(LoginView):
  template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
  next_page = '/'
    
