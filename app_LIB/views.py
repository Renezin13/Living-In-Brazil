from django.shortcuts import render
from django.http import HttpResponse
from .models import tb_pontosTuristicos, tb_enderecoTuristico, tb_galeira_pontos_turisticos


# Create your views here.

def home(request):
    return render(request, 'app_LIB/index.html')

def pontos_turisticos(request):

    pontos = {
        "pontos": tb_pontosTuristicos.objects.all()
    }
    return render(request, 'app_LIB/pontos_turisticos.html', pontos)

def login(request):
    return render(request, 'app_LIB/login.html')

def pt_descricao(request, id):
    ponto = tb_pontosTuristicos.objects.get(pon_id=id)
    endereco = tb_enderecoTuristico.objects.get(end_pon_id=ponto)
    galeria = tb_galeira_pontos_turisticos.objects.filter(gap_pon=ponto)

    objeto = {
        'ponto': ponto,
        'endereco': endereco,
        'galeria': galeria,
    }

    return render(request, 'app_LIB/pt_descricao.html', objeto)