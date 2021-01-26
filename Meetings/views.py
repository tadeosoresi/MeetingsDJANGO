from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

#Renderización de los html (templates)
def home(request):
    return render(request, "Meetings/index.html")

def shop(request):
    return render(request, "Meetings/shop.html")

def register(request):
    return render(request, "Meetings/registro.html")

def hidden(request):
    return render(request, "Meetings/hidden.html")

def rooftop(request):
    return render(request, "Meetings/rooftop.html")



def registro(request):
    form = UserCreationForm()
    if request.method == 'POST':

        '''name = request.POST['nombre_registro']
        surname = request.POST['apellido_registro']
        user = request.POST['usuario_registro']
        email = request.POST['email_registro']
        tel = request.POST['tel_registro']'''

        return(request, "Meetings/registro.html")

    return render(request, "Meetings/registro.html")