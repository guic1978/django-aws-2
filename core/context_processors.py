# -*- encoding: utf-8 -*-
from .models import Menu

def get_menus(request):
    try:
        menu_footer = Menu.objects.filter(ativo=True,local="FOOTER")[0]
    except:
        menu_footer = False

    return {
            'menu_footer': menu_footer,
        }