from django.forms import ModelForm
from .models import Produto, ProdutoImagem, Categoria
from django import forms

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        categoria = forms.ModelMultipleChoiceField(queryset=Categoria.objects.all(),widget=forms.CheckboxSelectMultiple(),required=True)
        fields = '__all__'

class ProdutoImagemForm(ModelForm):
    class Meta:
        model = ProdutoImagem
        fields = ['imagem','imagem_principal']