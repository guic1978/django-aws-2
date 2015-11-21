import os
from django.conf import settings
from django.shortcuts import render, RequestContext, Http404

from produtos.models import Produto

def home(request):
    produtos_destaque = Produto.objects.filter(ativo=True,destaque=True)
    produtos_novidades = Produto.objects.filter(ativo=True).order_by('-created_at')
    return render(request, "home.html", locals())