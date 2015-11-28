# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Noticia, Menu, ItemMenu, Pagina, GrupoItemMenu
from forms import NoticiaForm, PaginaForm

class NoticiaAdmin(admin.ModelAdmin):
    form = NoticiaForm
    prepopulated_fields = {"slug": ('titulo',)}

    class Meta:
        model = Noticia

admin.site.register(Noticia, NoticiaAdmin)


class ItemMenuInline(admin.TabularInline):
    model = ItemMenu

class GrupoItemMenuInline(admin.TabularInline):
    model = GrupoItemMenu.menus.through

class GrupoItemMenuAdmin(admin.ModelAdmin):
    inlines = [ItemMenuInline]
    class Meta:
        model = GrupoItemMenu

admin.site.register(GrupoItemMenu, GrupoItemMenuAdmin)

class MenuAdmin(admin.ModelAdmin):
    inlines = [GrupoItemMenuInline]

    class Meta:
        model = Menu

admin.site.register(Menu, MenuAdmin)

class ItemMenuAdmin(admin.ModelAdmin):
    list_display = ['nome','pagina','link','is_link']

    class Meta:
        model = ItemMenu

    # def paginas_do_item(self, obj):
    #
    #     pag = []
    #     for pagina in obj.paginas.all():
    #         link = "<a href='" + pagina.get_absolute_url() + "'>" + pagina.nome +  "</a>"
    #         pag.append(link)
    #         print link
    #     return ", ".join(pag)

    # paginas_do_item.allow_tags = True

admin.site.register(ItemMenu, ItemMenuAdmin)

class PaginaAdmin(admin.ModelAdmin):
    list_display = ['nome','titulo','slug','ativo','link']
    form = PaginaForm
    prepopulated_fields = {"slug": ('nome',)}

    class Meta:
        model = Pagina

    def link(self, obj):
        return "<a href='" + obj.get_absolute_url() + u"'>Ver Página</a>"

    link.allow_tags = True

admin.site.register(Pagina, PaginaAdmin)