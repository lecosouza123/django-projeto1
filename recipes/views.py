from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse('HOME 2')


def contato(request):
    return HttpResponse('contatoTeste')


def sobre(request):
    return HttpResponse('SOBRE')
