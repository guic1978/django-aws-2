"""encontreaqui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
# from django.views.generic import TemplateView
from registration.forms import RegistrationFormUniqueEmail
from registration.backends.default.views import RegistrationView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', "encontreaqui.views.home", name="home"),

    url(r'^ajax_view-product/(?P<produto_id>.*)', "produtos.views.produto_ajax_quick_view", name="ajax-view-product"),
    url(r'^produtos/', "produtos.views.produtos", name="produtos"),
    url(r'^produto/([0-9]+)/$', "produtos.views.produto", name="item_produto"),
    url(r'^produto/([0-9]+)/editar/', "produtos.views.editar_produto", name="editar_produto"),
    url(r'^produto/incluir/', "produtos.views.incluir_produto", name="incluir_produto"),
    url(r'^produto/([0-9]+)/imagens/', "produtos.views.gerenciar_imagem_produto", name="editar_imagem"),
    url(r'^produto/(?P<produto_id>.*)/download/(?P<filename>.*)$', "produtos.views.download_produto", name="download_produto"),

    url(r'^categoria/(?P<slug>.*)/$', "produtos.views.categoria", name="categoria"),

    url(r'^busca/', "produtos.views.buscar", name="busca_produtos"),

    url(r'^lib/', "perfis.views.library", name="library"),

    url(r'^carrinho/alterar/(?P<produto_id>.*)', "carrinho.views.alterar_carrinho", name="alterar_carrinho"),
    url(r'^carrinho/', "carrinho.views.carrinho", name="carrinho"),

    url(r'^noticias', 'core.views.todas_noticias', name='noticias' ),
    url(r'^noticias/(?P<ano>\d{4})$', 'core.views.noticias_ano', name='noticias_ano' ),
    url(r'^noticias/(?P<ano>\d{4})/(?P<mes>\d{2})$', 'core.views.noticias_mes', name='noticias_mes' ),
    url(r'^noticia/(?P<ano>\d{4})/(?P<mes>\d{2})/(?P<slug>.*)$', 'core.views.noticia', name='noticia' ),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),

    url(r'^accounts/', include('registration.backends.hmac.urls')),

    # url(r'^accounts/register/$',
    #     RegistrationView.as_view(form_class=RegistrationFormUniqueEmail),
    #     name='registration_register'),
]


