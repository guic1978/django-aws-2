# -*- encoding: utf-8 -*-
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

OPERACAO = (
    ("S", "SALVAR"),
    ("D", "DELETAR"),
    ("A", "ALTERAR"),
)

class Historico(models.Model):
    usuario = models.ForeignKey(User)
    modelo = models.CharField(max_length=20)
    operacao = models.CharField(max_length=1, choices=OPERACAO)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Criado em")

    def __unicode__(self):
		return u"Usuário: %s, Modelo: %s, Operação: %s" %(self.usuario, self.modelo, self.operacao)

class NoticiaManager(models.Manager):
    def all(self):
        return super(NoticiaManager, self).filter(ativo=True)

    def get_noticias_destaque(self):
        return self.all.filter(destaque=True).filter(data_expiracao__gt = datetime.datetime.now())

    def get_noticias_ano(self, ano):
        return self.all.filter(data_publicacao__year = ano)

    def get_noticias_mes(self, ano, mes):
        return self.all.filter(data_publicacao__year = ano).filter(data_publicacao__month = mes)

class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    titulo_curto = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField()
    conteudo = models.TextField(null=True, blank=True, verbose_name="Conteúdo")
    autor = models.ForeignKey(User, null=True, blank=True)
    data_publicacao = models.DateTimeField()
    data_expiracao = models.DateTimeField()
    ativo = models.BooleanField(default=True)
    destaque = models.BooleanField(default=False)
    imagem = models.ImageField(upload_to="produtos/image/", verbose_name="Imagem (420x450)", null=True, blank=True)
    imagem_150x150 = ImageSpecField(source='imagem',
                                      processors=[ResizeToFit(150, 150, mat_color=(245,245,245)),
                                                ],
                                      format='JPEG',
                                      options={'quality': 75})
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Alterado")


    def get_absolute_url(self):
        ano = self.data_publicacao.strftime("%Y")
        mes = self.data_publicacao.strftime("%m")
        return reverse('noticia', args=[ano, mes, self.slug])

    def get_ano_url(self):
        ano = self.data_publicacao.strftime("%Y")
        return reverse('noticias_ano', args=[ano])

    def get_mes_url(self):
        ano = self.data_publicacao.strftime("%Y")
        mes = self.data_publicacao.strftime("%m")
        return reverse('noticias_mes', args=[ano,mes])

    class Meta:
        ordering = ['-data_publicacao']

    def __unicode__(self):
    	return self.titulo