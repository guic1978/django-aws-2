# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Produto, Categoria, Tag, ProdutoImagem, \
    CategoriaImagem, Destaque, CategoriaBannerImagem, AtributoGrupo,\
    Atributo, ItemAtributo, ProdutoAtributo
from mptt.admin import MPTTModelAdmin
from django import forms
from mptt.forms import TreeNodeChoiceField
from django_mptt_admin.admin import DjangoMpttAdmin
from django.forms import ModelChoiceField
from .forms import ProdutoForm, ProdutoAtributoInLineForm
from django.utils.safestring import mark_safe

# PRODUTO
class TreeModelInlineForm(forms.ModelForm):
    categoria = TreeNodeChoiceField(queryset=Categoria.objects.all())

class CategoriaProdutoInline(admin.TabularInline):
    model = Categoria.produtos.through
    form = TreeModelInlineForm
    extra = 2

# class ProdutoAtributoAdmin(admin.ModelAdmin):
#     class Meta:
#         model = ProdutoAtributo

# admin.site.register(ProdutoAtributo, ProdutoAtributoAdmin)

class ProdutoImagemInLine(admin.StackedInline):
    extra = 2
    model = ProdutoImagem
    readonly_fields = ("Thumbnail",)
    fields = ('Thumbnail','titulo','imagem_principal','imagem')

    def Thumbnail(self, obj):
        return mark_safe('<img src="%s" />' %(obj.imagem_170x220.url))

class TagInLine(admin.StackedInline):
    prepopulated_fields = {"slug": ('nome',)}
    extra = 1
    model = Tag

class ProdutoAtributoInLine(admin.StackedInline):
    model = ProdutoAtributo
    # readonly_fields = ['atributo']
    fields = ['atributo','valor_item_atributo']
    readonly_fields = ['atributo']
    extra = 0
    form = ProdutoAtributoInLineForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "atributo":
            try:
                atributo_grupo = request._obj_.grupo_atributo #Obtem o grupo de atributo do produto
                kwargs["queryset"] = Atributo.objects.filter(atributogrupo=atributo_grupo)
            except:
                pass

        if db_field.name == "valor_item_atributo":
            try:
                kwargs["queryset"] = ItemAtributo.objects.filter(atributo=self.instance.atributo)
            except:
                kwargs["queryset"] = ItemAtributo.objects.all()

        return super(ProdutoAtributoInLine, self).formfield_for_foreignkey(db_field, request, **kwargs)

class ProdutoAdmin(admin.ModelAdmin):
    form = ProdutoForm
    list_display = ('imagem_principal_href','__unicode__','sku', 'preco', 'preco_desconto', 'ativo', 'categorias', 'created_at', 'link')
    inlines = [CategoriaProdutoInline, ProdutoAtributoInLine, ProdutoImagemInLine, TagInLine]
    search_fields = ('nome', 'sku', 'categoria__nome')
    prepopulated_fields = {"slug": ('nome',)}
    ordering = ('-created_at',)
    readonly_fields = ['link']
    fields = ('usuario','nome','descricao','ativo','preco','preco_desconto','slug','grupo_atributo')

    def get_form(self, request, obj=None, **kwargs):
        # just save obj reference for future processing in Inline
        request._obj_ = obj
        return super(ProdutoAdmin, self).get_form(request, obj, **kwargs)

    class Meta:
        model = Produto



    # def get_categorias(self, obj):
    #     return "\n".join([c.categorias for c in obj.categoria_set.all()])

    def categorias(self, obj):
        cat = []
        for i in obj.categoria_set.all():
            link = "<a href='/admin/produtos/categoria/" + str(i.id) + "'>" + i.nome +  "</a>"
            cat.append(link)
        return ", ".join(cat)

    categorias.allow_tags = True

    def link(self, obj):
        return "<a href='/produto/" + str(obj.id) + "'>Ver Produto</a>"

    link.allow_tags = True

class ProdutosDestaquesAdmin(admin.ModelAdmin):
    list_display = ('titulo','descricao', 'inicio', 'fim', 'ativo', 'default')
    class Meta:
        model = Destaque

# CATEGORIA
class CategoriaImagemInLine(admin.StackedInline):
    extra = 1
    model = CategoriaImagem

class CategoriaBannerImagemInLine(admin.StackedInline):
    extra = 1
    model = CategoriaBannerImagem

class CustomMPTTModelAdmin(DjangoMpttAdmin):
    list_display = ('nome','slug','total_produtos','mostra_menu','ordem_menu')
    inlines = [CategoriaImagemInLine, CategoriaBannerImagemInLine]
    fields = ('nome','descricao','slug','ativo','parent','mostra_menu','ordem_menu')
    prepopulated_fields = {"slug": ('nome',)}
    mptt_level_indent = 20

# ATRIBUTO
class AtributoGrupoAdmin(admin.ModelAdmin):
    list_display = ('nome','atributos_do_grupo')
    filter_horizontal = ['atributos']

    def atributos_do_grupo(self, obj):
        atributos = []
        for i in obj.atributos.all():
            link = str(i)
            atributos.append(link)
        return ", ".join(atributos)

    class Meta:
        model = AtributoGrupo

class ItemAtributoInLine(admin.StackedInline):
    extra = 4
    model = ItemAtributo
    prepopulated_fields = {"slug": ('valor',)}

class AtributoAdmin(admin.ModelAdmin):
    list_display = ('nome','nome_display','slug','filtra')
    inlines = [ItemAtributoInLine]
    prepopulated_fields = {"slug": ('nome',)}

    class Meta:
        model = Atributo

#REGISTER
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CustomMPTTModelAdmin)
admin.site.register(Destaque, ProdutosDestaquesAdmin)
admin.site.register(AtributoGrupo, AtributoGrupoAdmin)
admin.site.register(Atributo, AtributoAdmin)
admin.site.register(Tag)














