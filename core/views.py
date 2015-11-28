# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, Http404
from core.models import Noticia

def todas_noticias(request):
    noticias = Noticia.objects.filter(ativo=True)
    return render(request, "core/lista_noticias.html", locals())

def noticias_ano(request, ano):
    noticias = Noticia.objects.filter(ativo=True,data_publicacao__year=ano)
    return render(request, "core/lista_noticias.html", locals())

def noticias_mes(request, ano, mes):
    noticias = Noticia.objects.filter(ativo=True,data_publicacao__year=ano).filter(data_publicacao__month=mes)
    return render(request, "core/lista_noticias.html", locals())

def noticia(request, ano, mes, slug):
    try:
        noticia = Noticia.objects.filter(data_publicacao__year=ano).filter(data_publicacao__month=mes).get(slug=slug)
    except Noticia.MultipleObjectsReturned:
        noticia = Noticia.objects.filter(data_publicacao__year=ano).filter(data_publicacao__month=mes).get(slug=slug)[0]
    except:
        raise Http404

    return render(request, "core/noticia.html", locals())