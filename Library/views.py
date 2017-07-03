from django.forms import ModelForm
from .models import *
from django.shortcuts import render,redirect,get_object_or_404

class AlocacaoForm(ModelForm):
    class Meta:
        model = EconocomAlocacao
        fields = ['data', 'equipe', 'colaborador', 'cliente', 'projeto', 'horasUtilizadas']


def alocacao_list(request, template_name='list.html'):
    alocacao = EconocomAlocacao.objects.all()
    alocacoes = {'lista': alocacao}
    return render(request, template_name, alocacoes)

def alocacao_new(request, template_name='form.html'):
    form = AlocacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_alocacao')
    return render(request, template_name, {'form': form})


def alocacao_edit(request, pk, template_name='form.html'):
    alocacao = get_object_or_404(EconocomAlocacao, pk=pk)
    if request.method == "POST":
        form = AlocacaoForm(request.POST, instance=alocacao)
        if form.is_valid():
            alocacao = form.save()
            return redirect('listar_alocacao')
    else:
        form = AlocacaoForm(instance=alocacao)
    return render(request, template_name, {'form': form})

def alocacao_remove(request, pk):
    alocacao = EconocomAlocacao.objects.get(pk=pk)
    if request.method == "POST":
        alocacao.delete()
        return redirect('listar_alocao')
    return render(request, 'delete.html', {'alocao': alocacao})
