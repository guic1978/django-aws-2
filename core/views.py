# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, Http404
from core.models import Noticia
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import utils

def todas_noticias(request):

    titulo = "Notícias"

    noticias_lista = Noticia.objects.filter(ativo=True)

    page = request.GET.get('page')

    paginator = Paginator(noticias_lista, 12)

    try:
        noticias = paginator.page(page)
    except PageNotAnInteger:
        noticias = paginator.page(1)
    except EmptyPage:
        noticias = paginator.page(paginator.num_pages)

    return render(request, "noticias/lista.html", locals())

def noticias_ano(request, ano):

    titulo = "Notícias de %s" %(int(ano))

    noticias_lista = Noticia.objects.filter(ativo=True,data_publicacao__year=ano)

    page = request.GET.get('page')

    paginator = Paginator(noticias_lista, 12)

    try:
        noticias = paginator.page(page)
    except PageNotAnInteger:
        noticias = paginator.page(1)
    except EmptyPage:
        noticias = paginator.page(paginator.num_pages)

    return render(request, "noticias/lista.html", locals())

def noticias_mes(request, ano, mes):

    titulo = "Notícias de %s de %s" %(utils.NOME_MES[int(mes)],int(ano))

    noticias_lista = Noticia.objects.filter(ativo=True,data_publicacao__year=ano).filter(data_publicacao__month=mes)

    page = request.GET.get('page')

    paginator = Paginator(noticias_lista, 12)

    try:
        noticias = paginator.page(page)
    except PageNotAnInteger:
        noticias = paginator.page(1)
    except EmptyPage:
        noticias = paginator.page(paginator.num_pages)


    return render(request, "noticias/lista.html", locals())

def noticia(request, ano, mes, slug):
    try:
        noticia = Noticia.objects.filter(data_publicacao__year=ano).filter(data_publicacao__month=mes).get(slug=slug)
    except Noticia.MultipleObjectsReturned:
        noticia = Noticia.objects.filter(data_publicacao__year=ano).filter(data_publicacao__month=mes).get(slug=slug)[0]
    except:
        raise Http404

    return render(request, "noticias/noticia.html", locals())