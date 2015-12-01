# -*- encoding: utf-8 -*-
from django.forms import ModelForm
from .models import Produto, ProdutoImagem, Categoria, ItemAtributo, ProdutoAtributo
from django import forms
from tinymce.widgets import TinyMCE
from django.forms.widgets import HiddenInput

class ProdutoForm(ModelForm):
    descricao = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 180}))
    class Meta:
        model = Produto
        categoria = forms.ModelMultipleChoiceField(queryset=Categoria.objects.all(),widget=forms.CheckboxSelectMultiple(),required=True)
        fields = '__all__'

class ProdutoImagemForm(ModelForm):

    class Meta:
        model = ProdutoImagem
        fields = ['imagem','imagem_principal']

class ProdutoAtributoInLineForm(ModelForm):
    def __init__(self, *args, **kwargs):
        try:
            atributo = kwargs.get('instance').atributo
        except:
            atributo = 1

        super(ProdutoAtributoInLineForm, self).__init__(*args, **kwargs)
        if atributo != 1:
            self.fields['valor_item_atributo'].queryset = ItemAtributo.objects.filter(atributo=atributo)

    class Meta:
        model = ProdutoAtributo
        fields = ['atributo','valor_item_atributo']

# class ProdutoAtributoForm(ModelForm):
#
#     class Meta:
#         model = ProdutoAtributo
#         fields = ['valor_item_atributo']
