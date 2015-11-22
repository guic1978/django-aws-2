import os
from django.conf import settings
from django.shortcuts import render, RequestContext, Http404

from produtos.models import Produto, Destaque

def home(request):
    destaque = Destaque.objects.all()[0]
    produtos_destaque = []
    for item in destaque.produtos.all():
        produtos_destaque.append(item)

    produtos_novidades = Produto.objects.filter(ativo=True).order_by('-created_at')

    return render(request, "home.html", locals())