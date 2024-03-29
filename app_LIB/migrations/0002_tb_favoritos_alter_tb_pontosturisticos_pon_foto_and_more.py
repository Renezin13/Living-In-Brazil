# Generated by Django 5.0 on 2024-01-10 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_LIB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_favoritos',
            fields=[
                ('fav_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='tb_pontosturisticos',
            name='pon_foto',
            field=models.ImageField(blank=True, upload_to='imgs/'),
        ),
        migrations.CreateModel(
            name='tb_enderecoTuristico',
            fields=[
                ('end_id', models.AutoField(primary_key=True, serialize=False)),
                ('end_cidade', models.CharField(max_length=100)),
                ('end_bairro', models.CharField(max_length=100)),
                ('end_rua', models.CharField(max_length=100)),
                ('end_numero', models.IntegerField()),
                ('pon_latitude', models.FloatField()),
                ('pon_longitude', models.FloatField()),
                ('end_pon_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_LIB.tb_pontosturisticos')),
            ],
        ),
    ]
