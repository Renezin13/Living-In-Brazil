from django.contrib import admin
from .models import tb_usuario_fisico , tb_usuario_juridico ,tb_pontosTuristicos, tb_enderecoTuristico, tb_favoritos, tb_galeira_pontos_turisticos, tb_avaliacoes

# Register your models here.

admin.site.register(tb_usuario_fisico)
admin.site.register(tb_usuario_juridico)
admin.site.register(tb_pontosTuristicos)
admin.site.register(tb_enderecoTuristico)
admin.site.register(tb_favoritos)
admin.site.register(tb_galeira_pontos_turisticos)
admin.site.register(tb_avaliacoes)
