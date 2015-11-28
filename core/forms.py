from django import forms
from tinymce.widgets import TinyMCE
from .models import Noticia, Pagina

class NoticiaForm(forms.ModelForm):
    conteudo = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 180}))

    class Meta:
        model = Noticia
        fields = ['titulo','titulo_curto','conteudo','slug','autor','ativo','data_publicacao','data_expiracao','destaque','imagem']

class PaginaForm(forms.ModelForm):
    conteudo = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 180}))

    class Meta:
        model = Pagina
        fields = ['nome','titulo','slug','conteudo','ativo']
