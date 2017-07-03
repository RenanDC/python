# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EconocomAlocacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('data', models.DateField()),
                ('equipe', models.TextField(max_length=150, blank=True, null=True, choices=[('Projetos', 'Monitoração'), ('PreVenda', 'Pre-Venda'), ('DAS', 'Fabrica de Software')])),
                ('colaborador', models.TextField(max_length=150, blank=True, null=True)),
                ('cliente', models.TextField(max_length=250, blank=True, null=True)),
                ('projeto', models.TextField(max_length=250, blank=True, null=True)),
                ('horasUtilizadas', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Livro',
        ),
    ]
