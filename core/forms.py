from django import forms
from tinymce.widgets import TinyMCE
from .models import Noticia

class NoticiaForm(forms.ModelForm):
    conteudo = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 80}))

    class Meta:
        model = Noticia
        fields = ['titulo','conteudo','slug','autor','ativo','data_publicacao','data_expiracao','destaque','imagem']