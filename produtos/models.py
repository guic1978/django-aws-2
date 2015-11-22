# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db.models import signals
from django.dispatch.dispatcher import receiver
from django.core.urlresolvers import reverse

local_protegido = settings.UPLOADS_PROTEGIDOS

def local_download(instance, filename):
    if instance.usuario.username:
        return "%s/download/%s" %(instance.usuario.username, filename)
    else:
        return "%s/download/%s" %("default", filename)

class Produto(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True)
    nome = models.CharField(max_length=255)
    descricao = models.TextField(null=True, blank=True, verbose_name="Descrição")
    download = models.FileField(upload_to=local_download, storage=FileSystemStorage(location=local_protegido), null=True, blank=True)
    descricao_curta = models.TextField(null=True, blank=True, verbose_name="Descrição Curta")
    especificacao = models.TextField(null=True, blank=True, verbose_name="Especificações")
    sku = models.IntegerField(null=True, blank=True)
    order = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    preco_desconto = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Alterado")

    class Meta:
        ordering = ['-order']

    def __unicode__(self):
    	return self.nome

    def preco_venda(self):
        if self.preco_desconto > 0:
            return self.preco_desconto
        else:
            return self.preco

    def imagem_principal(self):
        imagemPrincipal = ProdutoImagem.objects.filter(produto = self.id)[:1].get()
        return imagemPrincipal

    def get_absolute_url(self):
        return reverse('produtos.views.produto', args=[self.id])

    def _get_mainCategory(self):
        """Return the first category for the product"""

        if self.categoria_set.count() > 0:
            return self.categoria_set.all()[0]
        else:
            return None

    categoria_principal = property(_get_mainCategory)

class ProdutoImagem(models.Model):
    produto = models.ForeignKey(Produto)
    imagem = models.ImageField(upload_to="produtos/image/")
    titulo = models.CharField(max_length=120, null=True, blank=True)
    imagem_principal = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Alterado")

    def __unicode__(self):
        return self.titulo

class Tag(models.Model):
    produto = models.ForeignKey(Produto)
    nome = models.CharField(max_length=50)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.nome

class CategoriaManager(models.Manager):
    def ativa(self, **kwargs):
        return self.filter(ativo=True, **kwargs)

class Categoria(models.Model):
    produto = models.ManyToManyField(Produto, null=True, blank=True)
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField()
    ativo = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='child', verbose_name="Categoria Pai")
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Alterado")
    objects = CategoriaManager()

    # @property
    # def filhas(self):
    # 	return Categoria.objects.all().filter(pai = self.id)

    def __unicode__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('produtos.views.categoria', args=[self.slug])

    def _recurse_for_parents(self, cat_obj):
        p_list = []
        if cat_obj.parent_id:
            p = cat_obj.parent
            p_list.append(p)
            if p != self:
                more = self._recurse_for_parents(p)
                p_list.extend(more)
        if cat_obj == self and p_list:
            p_list.reverse()
        return p_list

    def parents(self):
        return self._recurse_for_parents(self)

    def _flatten(self, L):
        """
        Taken from a python newsgroup post
        """
        if type(L) != type([]): return [L]
        if L == []: return L
        return self._flatten(L[0]) + self._flatten(L[1:])

    def _recurse_for_children(self, node, only_active=False):
        children = []
        children.append(node)
        for child in node.child.ativa():
            if child != self:
                # if (not only_active) or child.active_products().count() > 0:
                if (not only_active) > 0:
                    children_list = self._recurse_for_children(child, only_active=only_active)
                    children.append(children_list)
        return children

    def get_active_children(self, include_self=False):
        """
        Gets a list of all of the children categories which have active products.
        """
        return self.get_all_children(only_active=False, include_self=include_self)

    def get_all_children(self, only_active=False, include_self=False):
        """
        Gets a list of all of the children categories.
        """
        children_list = self._recurse_for_children(self, only_active=only_active)
        if include_self:
            ix = 0
        else:
            ix = 1
        flat_list = self._flatten(children_list[ix:])
        return flat_list

    # def active_products(self, variations=False, include_children=False, **kwargs):
    #     """Variations determines whether or not product variations are included
    #     in most templates we are not returning all variations, just the parent product.
    #     """
    #     site = Site.objects.get_current()
    #
    #     if not include_children:
    #         qry = self.product_set.filter(site=site)
    #     else:
    #         cats = self.get_all_children(include_self=True)
    #         qry = Product.objects.filter(site=site, category__in=cats)
    #
    #     if variations:
    #         slugs = qry.filter(site=site, active=True, **kwargs).values_list('slug',flat=True)
    #         return Product.objects.filter(Q(productvariation__parent__product__slug__in = slugs)|Q(slug__in = slugs)).prefetch_related('productimage_set')
    #     else:
    #         return qry.filter(site=site, active=True, productvariation__parent__isnull=True, **kwargs).prefetch_related('productimage_set')

def get_active_tree(include_self=True):
    """
    Gets a list of all of the children categories which have active products.
    """
    categoria = Categoria.objects.get(slug="raiz")

    return categoria.get_all_children(only_active=True, include_self=include_self)

class CategoriaImagem(models.Model):
    categoria = models.ForeignKey(Categoria, null=True)
    imagem = models.ImageField(upload_to="produtos/image/")
    titulo = models.CharField(max_length=120, null=True, blank=True)
    imagem_principal = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Alterado")

    def __unicode__(self):
        return self.titulo

# @receiver(signals.post_save, sender=Produto)
# def atualizar_historico_save(sender, instance, **kwargs):
#     historico = Historico(usuario=instance.carrinho.user, modelo="carrinho", operacao="S")
#     historico.save()
#
# @receiver(signals.post_delete, sender=Produto)
# def atualizar_historico_delete(sender, instance, **kwargs):
#     historico = Historico(usuario=instance.carrinho.user, modelo="carrinho", operacao="D")
#     historico.save()

class Destaque(models.Model):
    titulo = models.CharField(max_length=120)
    produtos = models.ManyToManyField(Produto, limit_choices_to={'ativo': True}, null=True, blank=True)
    inicio = models.DateField(auto_now_add=False, auto_now=False)
    fim = models.DateField(auto_now_add=False, auto_now=False)
    ativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Alterado")

    def __unicode__(self):
        return self.titulo

    def get_destaques(self):
        return self.produtos[:2]