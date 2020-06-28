from django.shortcuts import render, HttpResponse

# Create your views here.

def paginaInicial(request):
    return render(request,"contas/home.html")
    #return HttpResponse("Bem vindo a pagina app de Contas")
def login(request):
    return render(request,"contas/login.html")
    #return HttpResponse("Pagina de Login")
def registro(request):
    return HttpResponse("Pagina de Registro")
