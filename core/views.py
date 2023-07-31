from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
# def index(request):
#     return redirect('/agenda/')
def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request,'Usuário ou senha inválido')
    return redirect('/')

    return


@login_required(login_url='/login/')
def lista_eventos(request):
    usuatio= request.user
    evento = Evento.objects.filter(usuario=usuatio)
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)

def eventos(request, titulo_evento):
    titulo_evento = titulo_evento
    return HttpResponse(f'<h1>Titulo do Evento {titulo_evento}<h1>')
