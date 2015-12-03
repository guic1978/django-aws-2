import os
from django.shortcuts import render, RequestContext, Http404
from django.db.models import Q
from produtos.models import Produto, Destaque, Categoria

def home(request):

    try:
        produtos_destaque = Destaque.objects.get_instancia_destaque()
    except:
        produtos_destaque = False

    try:
        produtos_novidades = Produto.objects.filter(
            Q(preco__gt=0)|
            Q(preco_desconto__gt=0)
        ).filter(ativo=True).order_by('-created_at')
    except:
        produtos_novidades = False

    return render(request, "home.html", locals())
