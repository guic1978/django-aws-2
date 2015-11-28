# -*- coding: utf-8 -*-
from django.forms import TextInput, Textarea, CheckboxInput, CheckboxSelectMultiple
from django.forms.widgets import Select
from django.contrib import admin
from django.db import models

class CustomAdmin(admin.ModelAdmin):
    save_on_top = True
    actions = None
    list_select_related = True
    formfield_overrides = {
        models.CharField: {'widget':  TextInput(attrs={'style':'width:70%;'})},
        models.URLField: {'widget':  TextInput(attrs={'style':'width:70%;'})},
        models.ForeignKey: {'widget': Select(attrs={'style':'width:70%;'})},
        models.TextField: {'widget': Textarea(attrs={'style':'text-align:justify;width:70%;'})},
        models.BooleanField: {'widget': CheckboxInput(attrs={'style':'margin-top: 4px;'})},
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

NOME_MES = {
    1:'Janeiro',
    2:'Fevereiro',
    3:'Março',
    4:'Abril',
    5:'Maio',
    6:'Junho',
    7:'Julho',
    8:'Agosto',
    9:'Setembro',
    10:'Outubro',
    11:'Novembro',
    12:'Dezembro',
}

def nome_mes(numero):
    return NOME_MES[numero]