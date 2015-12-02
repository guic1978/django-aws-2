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
# from produtos.models import get_active_tree
from .models import Produto, Categoria, ProdutoImagem, ProdutoAtributo
from .forms import ProdutoForm, ProdutoImagemForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    try:
        produto = Produto.objects.get(pk=produto_id)
    except:
        raise Http404

    imagem_principal = ProdutoImagem.objects.get_imagem_principal(produto)
    downloadable = _checar_produto_comprado(request.user, produto)

    produtos_relacionados = []
    for categoria in produto.categoria_set.all():
        categoria.categoriabannerimagem_set.all()
        produtos_categoria = categoria.produtos.all()
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
    '''
    Retorna os produtos da busca

    :param request:
    :return:
    '''
    try:
        search = request.GET.get('busca', '')
    except:
        search = False

    produto_queryset = Produto.objects.filter(
        Q(nome__icontains=search)|
        Q(descricao_curta__icontains=search)
    ).filter(
        Q(preco__gt=0)|
        Q(preco_desconto__gt=0)
    ).filter(ativo=True)
    # categoria_queryset = Categoria.objects.filter(
    #     Q(nome__icontains=search)|
    #     Q(descricao__icontains=search)
    # )

    produtos_list = produto_queryset

    page = request.GET.get('page')
    try:
        per_page = int(request.REQUEST['page'])
    except:
        per_page = 16     # default value

    paginator = Paginator(produtos_list, 16)

    try:
        produtos = paginator.page(page)
    except PageNotAnInteger:
        produtos = paginator.page(1)
    except EmptyPage:
        produtos = paginator.page(paginator.num_pages)

    return render(request, "produtos/resultado_busca.html", locals())

def categoria(request, slug):
    '''
    Retorna os produtos da categoria.

    :param request:
    :param slug:
    :return:
    '''
    try:
        categoria = Categoria.objects.get(slug=slug)
    except:
        raise Http404

    #Obtem o filtro via querystring
    if request.GET.get('f'):
        filtro = request.GET.get('f').split('__')
    else:
        filtro = False


    #Obtem a ordem via qerystring
    if request.GET.get('o'):
        o = request.GET.get('o')
    else:
        o = "preco"     # default value

    if filtro:
        produtos_list = categoria.produtos.filter(
            Q(preco__gt=0)|
            Q(preco_desconto__gt=0)
        ).filter(ativo=True).order_by(o)\
            .filter(produtoatributo__atributo__slug=filtro[0])\
            .filter(produtoatributo__valor_item_atributo__slug=filtro[1])
    else:
        produtos_list = categoria.produtos.filter(
            Q(preco__gt=0)|
            Q(preco_desconto__gt=0)
        ).filter(ativo=True).order_by(o)

    categorias_relacionadas = Categoria.objects.filter(produtos=produtos_list)
    
    try:
        atributos_relaciondados = ProdutoAtributo.objects.filter(produto__in=produtos_list)
    except:
        atributos_relaciondados = False

    if atributos_relaciondados:
        atributos_dicionario = dict()
        distinct_atributo = []
        for atribut in atributos_relaciondados:
            if atribut.atributo in atributos_dicionario.keys():
                if atribut.valor_item_atributo.valor not in distinct_atributo:
                    distinct_atributo.append(atribut.valor_item_atributo.valor)
                    atributos_dicionario[atribut.atributo].append(atribut.valor_item_atributo)
            else:
                distinct_atributo = [atribut.valor_item_atributo.valor]
                atributos_dicionario[atribut.atributo] = [atribut.valor_item_atributo] # [(atribut.valor_item_atributo.valor,1)]

    try:
        todas_categorias = Categoria.objects.all()
    except:
        todas_categorias = False

    page = request.GET.get('page')

    try:
        per_page = int(request.GET.get('pp'))
    except:
        per_page = 16     # default value

    paginator = Paginator(produtos_list, per_page)

    try:
        produtos = paginator.page(page)
    except PageNotAnInteger:
        produtos = paginator.page(1)
    except EmptyPage:
        produtos = paginator.page(paginator.num_pages)

    return render(request, "produtos/produtos_categoria.html", locals())

def produto_ajax_quick_view(request, produto_id):
    try:
        produto = Produto.objects.get(pk=produto_id)
    except:
        produto = False

    return render_to_response("produtos/_ajax_view-product.html", locals(), context_instance=RequestContext(request))
