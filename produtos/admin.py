# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Produto, Categoria, Tag, ProdutoImagem, CategoriaImagem, Destaque, CategoriaBannerImagem
from mptt.admin import MPTTModelAdmin

class CategoriaImagemInLine(admin.StackedInline):
    extra = 1
    model = CategoriaImagem

class CategoriaBannerImagemInLine(admin.StackedInline):
    extra = 1
    model = CategoriaBannerImagem

class CategoriaProdutoInline(admin.TabularInline):
    model = Categoria.produto.through

class TagInLine(admin.StackedInline):
    prepopulated_fields = {"slug": ('nome',)}
    extra = 1
    model = Tag

class ImagemInLine(admin.StackedInline):
    extra = 3
    model = ProdutoImagem
    # raw_id_fields = ("imagem",)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','sku','descricao_curta', 'preco', 'preco_desconto', 'ativo', 'categorias', 'link')
    inlines = [CategoriaProdutoInline, ImagemInLine, TagInLine]
    search_fields = ('nome', 'sku', 'categoria__nome')
    list_filter = ('preco', 'created_at')
    prepopulated_fields = {"slug": ('nome',)}
    readonly_fields = ['link']
    fields = ('usuario','nome','descricao','ativo','preco','preco_desconto','slug')

    class Meta:
        model = Produto

    def get_categorias(self, obj):
        return "\n".join([c.categorias for c in obj.categoria_set.all()])

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

admin.site.register(Produto, ProdutoAdmin)

class CustomMPTTModelAdmin(MPTTModelAdmin):
    list_display = ('nome','slug','total_produtos','mostra_menu','ordem_menu')
    inlines = [CategoriaImagemInLine, CategoriaBannerImagemInLine]
    fields = ('nome','descricao','slug','ativo','parent','mostra_menu','ordem_menu')
    prepopulated_fields = {"slug": ('nome',)}
    mptt_level_indent = 20

admin.site.register(Categoria, CustomMPTTModelAdmin)

# class CategoriaAdmin(admin.ModelAdmin):
#     list_display = ('nome','slug')
#     inlines = [CategoriaImagemInLine, CategoriaBannerImagemInLine]
#     prepopulated_fields = {"slug": ('nome',)}
#     class Meta:
#         model = Categoria
#
# admin.site.register(Categoria, CategoriaAdmin)

admin.site.register(Tag)

class ProdutosDestaquesAdmin(admin.ModelAdmin):
    list_display = ('titulo','descricao', 'inicio', 'fim', 'ativo', 'default')
    class Meta:
        model = Destaque

admin.site.register(Destaque, ProdutosDestaquesAdmin)
