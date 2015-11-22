# -*- encoding: utf-8 -*-
import os
import json
from itertools import chain
from mimetypes import guess_type

from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, render_to_response, RequestContext
from django.template.defaultfilters import slugify
from django.forms import modelformset_factory
from django.core.servers.basehttp import FileWrapper
from django.db.models import Q
from produtos.models import get_active_tree
from .models import Produto, Categoria, ProdutoImagem
from .forms import ProdutoForm, ProdutoImagemForm

def _checar_produto_comprado(user, produto):
    if user.is_authenticated():
        try:
            if produto in user.usuariocompra.produtos.all():
                return True
            else:
                return False
        except:
            return False
    else:
        return False

def download_produto(request, produto_id, filename):
    produto = Produto.objects.get(pk=produto_id)

    if _checar_produto_comprado(request.user, produto):
        arquivo =str(produto.download)
        caminho_arquivo = os.path.join(settings.UPLOADS_PROTEGIDOS, arquivo)
        wrapper = FileWrapper(file(caminho_arquivo))
        response = HttpResponse(wrapper, content_type=guess_type(arquivo))
        response['Content-Diposition'] = 'attachment;filename=%s' %filename
        response['Content-Type'] = ''
        response['X-SendFile'] = caminho_arquivo
        return response
    else:
        raise Http404

    # return render(request, "produtos/mostra_produto.html", locals())

def produtos(request):
    produtos = Produto.objects.all()
    return render(request, "produtos/lista_produtos.html", locals())

def produto(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    downloadable = _checar_produto_comprado(request.user, produto)

    produtos_relacionados = []
    for categoria in produto.categoria_set.all():
        produtos_categoria = categoria.produto.all()
        for item in produtos_categoria:
            if (not item == produto) and (item not in produtos_relacionados):
                produtos_relacionados.append(item)

    return render(request, "produtos/mostra_produto.html", locals())

def incluir_produto(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        produto = form.save(commit=False)
        produto.usuario = request.user
        produto.slug = slugify(form.cleaned_data['nome'])
        produto.save()
        return HttpResponseRedirect('/produto/%s'%(produto.id))

    return render(request, "produtos/editar.html", locals())

def gerenciar_imagem_produto(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    queryset = ProdutoImagem.objects.filter(produto = produto)
    ProdutoImagemFormset = modelformset_factory(ProdutoImagem, form=ProdutoImagemForm, can_delete=True)
    formset = ProdutoImagemFormset(request.POST or None,queryset=queryset)
    form = ProdutoImagemForm(request.POST or None)
    MEDIA_URL = settings.MEDIA_URL

    if formset.is_valid():
        for form in formset:
            instance = form.save(commit=False)
            instance.produto = produto
            instance.save()
        if formset.deleted_forms:
            formset.save()

    return render(request, "produtos/editar_imagem.html", locals())


def editar_produto(request, produto_id):
    instance = Produto.objects.get(pk=produto_id)
    form = ProdutoForm(request.POST or None, instance=instance)
    if form.is_valid():
        produto_edit = form.save()

    return render(request, "produtos/editar.html", locals())

def buscar(request):
    try:
        search = request.GET.get('busca', '')
    except:
        search = False

    produto_queryset = Produto.objects.filter(
        Q(nome__icontains=search)|
        Q(descricao_curta__icontains=search)
    )
    # categoria_queryset = Categoria.objects.filter(
    #     Q(nome__icontains=search)|
    #     Q(descricao__icontains=search)
    # )

    # produtos = list(chain(produto_queryset, categoria_queryset))
    produtos = produto_queryset

    #
    # if search:
    #     palavras = search.split()
    #     if len(palavras) >= 2:
    #         produtos = []
    #         for item in palavras:
    #             todos_produtos = Produto.objects.filter(nome__icontains=item).distinct()
    #             for produto in todos_produtos:
    #                 if produto not in produtos:
    #                     produtos.append(produto)
    #     else:
    #         produtos = Produto.objects.filter(nome__icontains=search)

    return render(request, "produtos/resultado_busca.html", locals())

def categoria(request, slug):
    try:
        categoria = Categoria.objects.get(slug=slug)
    except:
        raise Http404

    # print categoria
    # print categoria.parents()
    # print categoria.get_all_children()

    produtos = categoria.produto.all()

    # print get_active_tree()

    categorias_relacionadas = []
    for produto in produtos:
        categorias_produto = produto.categoria_set.all()
        for item_categoria in categorias_produto:
            if (not item_categoria == categoria) and (item_categoria not in categorias_relacionadas):
                categorias_relacionadas.append(item_categoria)

    try:
        todas_categorias = Categoria.objects.all
    except:
        todas_categorias = False


    return render(request, "produtos/produtos_categoria.html", locals())

def produto_ajax_quick_view(request, produto_id):
    try:
        produto = Produto.objects.get(pk=produto_id)
    except:
        produto = False

    return render_to_response("produtos/_ajax_view-product.html", locals(), context_instance=RequestContext(request))
