# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.signals import user_logged_in
# from django.dispatch.dispatcher import receiver

from produtos.models import Produto
# from encontreaqui.stripe import secret_key

# import stripe

# stripe.api_key = secret_key

# class UsuarioStripe(models.Model):
#     usuario = models.OneToOneField(User)
#     stripe_id = models.CharField(max_length=120, null=True, blank=True)
#
#     def __unicode__(self):
#         return self.usuario.username
#
# @receiver([user_logged_in])
# def CriarStripe_Id(sender, user, request, **Kwargs):
#     new_stripe_id, created = UsuarioStripe.objects.get_or_create(usuario=user)
#     if created:
#         stripe_cust = stripe.Customer.create(email=user.email, description="Usuário criado pela aplicação")
#         new_stripe_id = stripe_cust.id
#         new_stripe_id.save()
#         # print stripe_cust.id

class UsuarioCompra(models.Model):
    usuario = models.OneToOneField(User)
    produtos = models.ManyToManyField(Produto)

    def __unicode__(self):
        return self.usuario.username

