# Generated by Django 5.0 on 2024-01-10 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_LIB', '0002_tb_favoritos_alter_tb_pontosturisticos_pon_foto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_pontosturisticos',
            name='pon_qrcode',
            field=models.ImageField(blank=True, upload_to='imgsPontos/'),
        ),
    ]
