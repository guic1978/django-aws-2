# -*- encoding: utf-8 -*-
from produtos.models import Categoria

def get_categorias_menu(request):

    try:
        categorias = Categoria.objects.get_categorias_menu()
    except:
        categorias = False

    return {
            'categorias_nodes': categorias,
        }
