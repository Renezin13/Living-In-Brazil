from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Avg
from django.db.models import Q
from .models import tb_pontosTuristicos, tb_enderecoTuristico, tb_galeira_pontos_turisticos, tb_avaliacoes, tb_favoritos, tb_usuario_fisico, tb_usuario_juridico


# Create your views here.

def home(request):
    return render(request, 'app_LIB/index.html')

def pontos_turisticos(request):

    pontos = {
        "pontos": tb_pontosTuristicos.objects.all()
    }

    pesquisa = request.GET.get('pesquisa')
    
    if pesquisa:
        pontos['pontos'] = pontos['pontos'].filter(
            Q(pon_nome__icontains=pesquisa)
            | Q(pon_descricao__icontains=pesquisa)
        )

    return render(request, 'app_LIB/pontos_turisticos.html', pontos)

def login(request):
    return render(request, 'app_LIB/login.html')

def pt_descricao(request, id):
    ponto = tb_pontosTuristicos.objects.get(pon_id=id)
    endereco = tb_enderecoTuristico.objects.get(end_pon_id=ponto)
    galeria = tb_galeira_pontos_turisticos.objects.filter(gap_pon=ponto)
    avaliacao = tb_avaliacoes.objects.filter(ava_pon_id=ponto).prefetch_related('ava_fis_id')

    media_notas = avaliacao.aggregate(media=Avg('ava_nota'))['media']

    objeto = {
        'ponto': ponto,
        'endereco': endereco,
        'galeria': galeria,
        'avaliacao': avaliacao,
        'media_notas': media_notas,
    }

    return render(request, 'app_LIB/pt_descricao.html', objeto)