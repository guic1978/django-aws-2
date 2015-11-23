# -*- encoding: utf-8 -*-
from .models import Carrinho

def checa_carrinho(request):
    # Verifica se há carrinho aberto na sessão
    try:
        carrinho_id = request.session["CARRINHO_ID"]
    except:
        carrinho_id = False

    if carrinho_id:
        carrinho = Carrinho.objects.get(id=carrinho_id)
    else:
        carrinho=False

    return {
            'carrinho_sessao': carrinho,
        }