from django.db import models

# Create your models here.

class EconocomAlocacao(models.Model):
    Equipe_Choise = (
            ('Projetos', 'Monitoração'),
            ('PreVenda', 'Pre-Venda'),
            ('DAS', 'Fabrica de Software'),
        )
    data = models.DateField()
    equipe = models.TextField(max_length=150, blank=True, null=True, choices=Equipe_Choise)
    colaborador = models.TextField(max_length=150, blank=True, null=True)
    cliente = models.TextField(max_length=250, blank=True, null=True)
    projeto = models.TextField(max_length=250, blank=True, null=True)
    horasUtilizadas = models.IntegerField(blank=True, null=True)
