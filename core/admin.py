# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Noticia
from forms import NoticiaForm

class NoticiaAdmin(admin.ModelAdmin):
    form = NoticiaForm
    prepopulated_fields = {"slug": ('titulo',)}
    # fields = '__all__'

    class Meta:
        model = Noticia

admin.site.register(Noticia, NoticiaAdmin)