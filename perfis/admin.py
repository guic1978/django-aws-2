from django.contrib import admin

from .models import UsuarioCompra, UsuarioStripe

class UsuarioCompraAdmin(admin.ModelAdmin):
    class Meta:
        model = UsuarioCompra

admin.site.register(UsuarioCompra, UsuarioCompraAdmin)

class UsuarioStripeAdmin(admin.ModelAdmin):
    class Meta:
        model = UsuarioStripe

admin.site.register(UsuarioStripe, UsuarioStripeAdmin)