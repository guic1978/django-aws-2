# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from mptt.models import MPTTModel, TreeForeignKey

import datetime

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
            return self.categoria_set.all().order_by('ordem_menu')[0]
        else:
            return None

    categoria_principal = property(_get_mainCategory)

class ProdutoImagemManager(models.Manager):
    def get_imagem_principal(self, produto):
        try:
            principal = super(ProdutoImagemManager, self).filter(produto=produto).filter(imagem_principal=True)[:1]
        except:
            principal = super(ProdutoImagemManager, self).filter(produto=produto)[:1]

        return principal[0]

class ProdutoImagem(models.Model):
    produto = models.ForeignKey(Produto)
    imagem = models.ImageField(upload_to="produtos/image/", verbose_name="Imagem (420x450)")
    imagem_65x75 = ImageSpecField(source='imagem',
                                      processors=[ResizeToFit(65, 75, mat_color=(245,245,245)),
                                                ],
                                      format='JPEG',
                                      options={'quality': 75})
    imagem_90x100 = ImageSpecField(source='imagem',
                                      processors=[ResizeToFit(90, 100, mat_color=(245,245,245))
                                                  ],
                                      format='JPEG',
                                      options={'quality': 75})
    imagem_90x90 = ImageSpecField(source='imagem',
                                      processors=[ResizeToFit(90, 90, mat_color=(245,245,245))
                                                  ],
                                      format='JPEG',
                                      options={'quality': 75})
    imagem_170x220 = ImageSpecField(source='imagem',
                                      processors=[ResizeToFit(170, 220, mat_color=(245,245,245)),
                                      ],
                                      format='JPEG',
                                      options={'quality': 75})
    imagem_252x269 = ImageSpecField(source='imagem',
                                      processors=[ResizeToFit(252, 269, mat_color=(245,245,245)),
                                                  ],
                                      format='JPEG',
                                      options={'quality': 75})
    imagem_390x390 = ImageSpecField(source='imagem',
                                      processors=[ResizeToFit(390, 390, mat_color=(245,245,245)),
                                                  ],
                                      format='JPEG',
                                      options={'quality': 75})
    imagem_450x450 = ImageSpecField(source='imagem',
                                      processors=[ResizeToFit(450, 450, mat_color=(245,245,245)),
                                                  ],
                                      format='JPEG',
                                      options={'quality': 75})

    titulo = models.CharField(max_length=120, null=True, blank=True)
    imagem_principal = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Alterado")
    objects = ProdutoImagemManager()

    def __unicode__(self):
        return self.titulo

class CategoriaManager(models.Manager):
    def ativa(self, **kwargs):
        return self.filter(ativo=True, **kwargs)

    def get_categorias_menu(self):
        return self.filter(ativo=True,mostra_menu=True)

class Categoria(MPTTModel):
    produtos = models.ManyToManyField(Produto, null=True, blank=True)
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField()
    ativo = models.BooleanField(default=True)
    mostra_menu = models.BooleanField(default=False)
    ordem_menu = models.IntegerField(default=0)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children',verbose_name="Categoria Pai")
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Alterado")
    objects = CategoriaManager()

    class MPTTMeta:
        order_insertion_by = ['ordem_menu']

    def __unicode__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('produtos.views.categoria', args=[self.slug])

    def total_produtos(self):
        return len(Produto.objects.filter(categoria=self))

class Tag(models.Model):
    produto = models.ForeignKey(Produto)
    nome = models.CharField(max_length=50)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.nome

# def get_active_tree(include_self=True):
#     """
#     Gets a list of all of the children categories which have active products.
#     """
#     categoria = Categoria.objects.get(slug="raiz")
#
#     return categoria.get_all_children(only_active=True, include_self=include_self)

class CategoriaImagem(models.Model):
    categoria = models.ForeignKey(Categoria, null=True)
    imagem = models.ImageField(upload_to="produtos/image/", null=True, blank=True, verbose_name="Imagem (100x100)")
    imagem_100x100 = ImageSpecField(source='imagem',
                                      processors=[ResizeToFit(100, 100, mat_color=(255,255,255)),
                                                ],
                                      format='JPEG',
                                      options={'quality': 75})
    titulo = models.CharField(max_length=120, null=True, blank=True)
    imagem_principal = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Alterado")

    def __unicode__(self):
        return self.titulo

class CategoriaBannerImagem(models.Model):
    categoria = models.ForeignKey(Categoria, null=True)
    imagem = models.ImageField(upload_to="produtos/image/", null=True, blank=True, verbose_name="Imagem (453x154)")
    imagem_453x154 = ImageSpecField(source='imagem',
                                      processors=[ResizeToFit(453, 154, mat_color=(255,255,255)),
                                                ],
                                      format='JPEG',
                                      options={'quality': 75})
    titulo = models.CharField(max_length=120, null=True, blank=True)
    imagem_principal = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Alterado")

    def __unicode__(self):
        return self.titulo

class DestaqueManager(models.Manager):
    def get_instancia_destaque(self):
        destaques_ativos_no_periodo = super(DestaqueManager, self).filter(inicio__lte=datetime.datetime.now()).filter(fim__gte=datetime.datetime.now()).filter(ativo=True)
        if len(destaques_ativos_no_periodo) > 0:
            return destaques_ativos_no_periodo[0]
        else:
            destaques_padrao = super(DestaqueManager, self).filter(default=True)
            return destaques_padrao[0]

class Destaque(models.Model):
    titulo = models.CharField(max_length=120)
    descricao = models.TextField(max_length=200, null=True, blank=True)
    produtos = models.ManyToManyField(Produto, limit_choices_to={'ativo': True}, null=True, blank=True)
    inicio = models.DateField(auto_now_add=False, auto_now=False)
    fim = models.DateField(auto_now_add=False, auto_now=False)
    ativo = models.BooleanField(default=True)
    default = models.BooleanField(default=False, verbose_name="Padrão")
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Alterado")

    objects = DestaqueManager()

    def __unicode__(self):
        return self.titulo

    def get_destaques(self):
        return self.produtos[:2]