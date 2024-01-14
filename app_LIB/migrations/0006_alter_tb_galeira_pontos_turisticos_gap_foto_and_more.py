# Generated by Django 5.0 on 2024-01-13 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_LIB', '0005_tb_galeira_pontos_turisticos_tb_favoritos_fav_pon_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_galeira_pontos_turisticos',
            name='gap_foto',
            field=models.ImageField(blank=True, upload_to='imgs_pon/'),
        ),
        migrations.AlterField(
            model_name='tb_pontosturisticos',
            name='pon_foto',
            field=models.ImageField(blank=True, upload_to='imgs_pon/'),
        ),
        migrations.AlterField(
            model_name='tb_pontosturisticos',
            name='pon_qrcode',
            field=models.ImageField(blank=True, upload_to='imgs_qr/'),
        ),
        migrations.AlterField(
            model_name='tb_usuario_fisico',
            name='fis_foto',
            field=models.ImageField(blank=True, upload_to='imgs_fis/'),
        ),
        migrations.AlterField(
            model_name='tb_usuario_juridico',
            name='jur_foto',
            field=models.ImageField(blank=True, upload_to='imgs_jur/'),
        ),
    ]