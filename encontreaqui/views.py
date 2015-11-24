import os
from django.shortcuts import render, RequestContext, Http404
from django.core.mail import EmailMessage

from produtos.models import Produto, Destaque

def home(request):
    produtos_destaque = Destaque.objects.get_instancia_destaque()
    produtos_novidades = Produto.objects.filter(ativo=True).order_by('-created_at')

    email = EmailMessage('Hello', 'World', to=['guilherme.guic@gmail.com'])
    email.send()

    return render(request, "home.html", locals())

