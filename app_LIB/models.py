from django.db import models
import PIL
from django.contrib.auth.models import User

class tb_usuario_fisico(models.Model):
    fis_user = models.OneToOneField(User, on_delete=models.CASCADE)
    fis_id = models.AutoField(primary_key=True)
    fis_foto = models.ImageField(upload_to='imgs_fis/', blank = True)
    fis_idade = models.IntegerField()
    fis_sexo = models.CharField(max_length=15)
    fis_nascimento = models.DateField()
    fis_profissao = models.CharField(max_length=100)
    fis_telefone = models.IntegerField()

class tb_usuario_juridico(models.Model):
    jur_user = models.OneToOneField(User, on_delete=models.CASCADE)
    jur_id = models.AutoField(primary_key=True)
    jur_nome_fantasia = models.CharField(max_length=100)
    jur_telefone = models.IntegerField()
    jur_foto = models.ImageField(upload_to='imgs_jur/',blank = True)

class tb_pontosTuristicos(models.Model):
    pon_id = models.AutoField(primary_key=True)
    pon_nome = models.CharField(max_length=100)
    pon_descricao = models.CharField(max_length=512)
    pon_foto = models.ImageField(upload_to='imgs_pon/', blank = True)
    pon_qrcode = models.ImageField(upload_to='imgs_qr/',blank = True)

class tb_enderecoTuristico(models.Model):
    end_id = models.AutoField(primary_key=True)
    end_pon_id = models.OneToOneField(tb_pontosTuristicos, on_delete=models.CASCADE)
    end_cidade = models.CharField(max_length=100)
    end_bairro = models.CharField(max_length=100)
    end_rua = models.CharField(max_length=100)
    end_numero = models.IntegerField()
    end_latitude = models.FloatField()
    end_longitude = models.FloatField()

class tb_galeira_pontos_turisticos(models.Model):
    gap_id = models.AutoField(primary_key=True)
    gap_descricao = models.CharField(max_length=512)
    gap_foto = models.ImageField(upload_to='imgs_pon/', blank = True)
    gap_pon = models.ForeignKey(tb_pontosTuristicos, on_delete=models.CASCADE)

class tb_favoritos(models.Model):
    fav_id = models.AutoField(primary_key=True)
    fav_fis_id = models.ForeignKey(tb_usuario_fisico, on_delete=models.CASCADE)
    fav_pon_id = models.ForeignKey(tb_pontosTuristicos, on_delete=models.CASCADE)
    
class tb_avaliacoes(models.Model):
    ava_id = models.AutoField(primary_key=True)
    ava_avaliacao = models.FloatField()
    ava_comentario = models.CharField(max_length=512)
    ava_fis_id = models.ForeignKey(tb_usuario_fisico, on_delete=models.CASCADE,)
    ava_nota = models.IntegerField()
    ava_pon_id = models.ForeignKey(tb_pontosTuristicos, on_delete=models.CASCADE)
