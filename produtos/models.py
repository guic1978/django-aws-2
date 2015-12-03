# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from mptt.models import MPTTModel, TreeForeignKey
from tinymce import models as tinymce_models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

import datetime

local_protegido = settings.UPLOADS_PROTEGIDOS

def local_download(instance, filename):
    if instance.usuario.username:
        return "%s/download/%s" %(instance.usuario.username, filename)
    else:
        return "%s/download/%s" %("default", filename)

# TIPO_ATRIBUTO = (
#     ("CAMPO_TEXTO", "CAMPO_TEXTO"),
#     ("SELECAO", "SELECAO"),
# )

class AtributoManager(models.Manager):
    def get_atributos_grupo_produto(self, produto):
        return super(AtributoManager, self).filter(atributogrupo__produto=produto)

class Atributo(models.Model): #Exemplo Cor, Marca, Modelo, Plataforma
    nome = models.CharField(max_length=50)
    nome_display = models.CharField(max_length=50)
    slug = models.SlugField()
    # tipo = models.CharField(max_length=35, choices=TIPO_ATRIBUTO, default="CAMPO_TEXTO") #Campo Texto ou por DropDown
    filtra = models.BooleanField(default=False)
    objects = AtributoManager()

    # def atributogrupos(self):
    #     return Atributo.objects.filter(atributogrupo__atributo=self)

    def __unicode__(self):
        return self.nome

class AtributoGrupo(models.Model):
    nome = models.CharField(max_length=50)
    atributos = models.ManyToManyField(Atributo) #para associar os atributos a um grupo

    def __unicode__(self):
        return self.nome

class ProdutoManager(models.Manager):
    def all_ativo_preco(self):
        return self.filter(ativo=True).filter(preco__gt=0)

    # def filter(self):
    #     return self.filter(ativo=True).filter(preco__lt=0)

class Produto(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True)
    nome = models.CharField(max_length=255)
    # descricao = models.TextField(null=True, blank=True, verbose_name="Descrição")
    descricao = tinymce_models.HTMLField(null=True, blank=True, verbose_name="Descrição")
    download = models.FileField(upload_to=local_download, storage=FileSystemStorage(location=local_protegido), null=True, blank=True)
    descricao_curta = models.TextField(null=True, blank=True, verbose_name="Descrição Curta")
    sku = models.IntegerField(null=True, blank=True)
    order = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    preco_desconto = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    slug = models.SlugField()
    grupo_atributo = models.ForeignKey(AtributoGrupo) #para listar os atributos disponíveis para o produto
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Alterado")
    objects = ProdutoManager()

    class Meta:
        ordering = ['-order']

    # Quando trocar o grpo atributo, apagar os valores dos objeto ProdutoAtributo

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

    def imagem_principal_href(self):
        imagemPrincipal = ProdutoImagem.objects.filter(produto = self.id)[:1].get()
        return '<img src="%s" title="%s" />' %(imagemPrincipal.imagem_65x75.url,imagemPrincipal.titulo)

    imagem_principal_href.allow_tags = True

    def get_absolute_url(self):
        return reverse('produtos.views.produto', args=[self.id])

    def _get_mainCategory(self):
        """Return the first category for the product"""

        if self.categoria_set.count() > 0:
            return self.categoria_set.all().order_by('ordem_menu')[0]
        else:
            return None

    categoria_principal = property(_get_mainCategory)

@receiver(pre_save, sender=Produto)
def zerar_atributos_produtos(sender, instance, **kwargs):
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass # Object is new, so field hasn't technically changed, but you may want to do something else here.
    else:
        try:
            if not obj.grupo_atributo == instance.grupo_atributo: # Field has changed

                try:
                    produtos_atributos = ProdutoAtributo.objects.filter(produto=instance) #apaga os atributos do produto
                    produtos_atributos.delete()
                except:
                    pass

                atributo_grupo = instance.grupo_atributo
                atributos = Atributo.objects.filter(atributogrupo=atributo_grupo)

                if atributos:
                    for atributo in atributos:
                        produtoatributo = ProdutoAtributo(produto=instance,atributo=atributo)
                        produtoatributo.save()
        except:
            try:
                produtos_atributos = ProdutoAtributo.objects.filter(produto=instance) #apaga os atributos do produto
                produtos_atributos.delete()
            except:
                pass

            atributo_grupo = instance.grupo_atributo
            atributos = Atributo.objects.filter(atributogrupo=atributo_grupo)

            if atributos:
                for atributo in atributos:
                    produtoatributo = ProdutoAtributo(produto=instance,atributo=atributo)
                    produtoatributo.save()

@receiver(post_save, sender=Produto)
def novos_atributos_produtos(sender, instance, **kwargs):
    try:
        atributos = ProdutoAtributo.objects.filter(produto = instance)
    except:
        atributos = False
    if not atributos:
        ProdutoAtributo.objects.filter(produto = instance).delete() #apaga os atributos do produto
        atributo_grupo = instance.grupo_atributo
        atributos = Atributo.objects.filter(atributogrupo=atributo_grupo)
        if atributos:
            for atributo in atributos:
                produtoatributo = ProdutoAtributo(produto=instance,atributo=atributo)
                produtoatributo.save()

class ProdutoImagemManager(models.Manager):
    def get_imagem_principal(self, produto):
        try:
            principal = super(ProdutoImagemManager, self).filter(produto=produto).filter(imagem_principal=True)[0]
        except:
            principal = super(ProdutoImagemManager, self).filter(produto=produto)[0]

        return principal

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

    def get_imagem_90x90(self):
        return '<img src="%s" title="%s" />' %(self.imagem_90x90.url,self.titulo)

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

# class CategoriaImagem(models.Model):
#     categoria = models.ForeignKey(Categoria, null=True)
#     imagem = models.ImageField(upload_to="produtos/image/", null=True, blank=True, verbose_name="Imagem (100x100)")
#     imagem_100x100 = ImageSpecField(source='imagem',
#                                       processors=[ResizeToFit(100, 100, mat_color=(255,255,255)),
#                                                 ],
#                                       format='JPEG',
#                                       options={'quality': 75})
#     titulo = models.CharField(max_length=120, null=True, blank=True)
#     imagem_principal = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Criado em")
#     updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Alterado")
#
#     def __unicode__(self):
#         return self.titulo

# class CategoriaBannerImagem(models.Model):
#     categoria = models.ForeignKey(Categoria, null=True)
#     imagem = models.ImageField(upload_to="produtos/image/", null=True, blank=True, verbose_name="Imagem (453x154)")
#     imagem_453x154 = ImageSpecField(source='imagem',
#                                       processors=[ResizeToFit(453, 154, mat_color=(255,255,255)),
#                                                 ],
#                                       format='JPEG',
#                                       options={'quality': 75})
#     titulo = models.CharField(max_length=120, null=True, blank=True)
#     imagem_principal = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Criado em")
#     updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Alterado")
#
#     def __unicode__(self):
#         return self.titulo

'''
Refatoração: Mover Destaque para o app Core
'''
class DestaqueManager(models.Manager):
    def get_instancia_destaque(self):
        destaques_ativos_no_periodo = super(DestaqueManager, self)\
            .filter(inicio__lte=datetime.datetime.now())\
            .filter(fim__gte=datetime.datetime.now())\
            .filter(ativo=True)

        if len(destaques_ativos_no_periodo) > 0:
            destaque = destaques_ativos_no_periodo[0]
        else:
            destaques_padrao = super(DestaqueManager, self).filter(default=True)
            destaque = destaques_padrao[0]

        produtos_destaques_ativos_preco = []
        for produto in destaque.produtos.all():
            if ((produto.preco > 0) | (produto.preco_desconto > 0)) and (produto.ativo == True):
                produtos_destaques_ativos_preco.append(produto)

        destaque.produtos = produtos_destaques_ativos_preco

        return destaque

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

class ItemAtributo(models.Model): #Exemplo Cor: Branca, Azul,, Preta; Marca: Sony, Microsoft;
    atributo = models.ForeignKey(Atributo)
    valor = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        unique_together = (("atributo", "slug"),)

    def __unicode__(self):
        return "%s" %(self.valor)
        # return "Atributo: %s, Valor: %s" %(self.atributo, self.valor)

class ProdutoAtributo(models.Model):
    produto = models.ForeignKey(Produto)
    atributo = models.ForeignKey(Atributo)
    valor_item_atributo = models.ForeignKey(ItemAtributo, null=True, blank=True, verbose_name="valor")

    def __unicode__(self):
        return "%s" %(self.atributo)
        # return "Produto: %s, Valor_item: %s" %(self.produto, self.valor_item_atributo)

    class Meta:
        unique_together = (("produto", "atributo"),)
