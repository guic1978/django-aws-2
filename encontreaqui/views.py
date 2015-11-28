import os
from django.shortcuts import render, RequestContext, Http404
# from registration.backends.hmac.views import RegistrationView
# from django.contrib.auth.models import User

from produtos.models import Produto, Destaque, Categoria

def home(request):
    produtos_destaque = Destaque.objects.get_instancia_destaque()
    produtos_novidades = Produto.objects.filter(ativo=True).order_by('-created_at')

    return render(request, "home.html", locals())
