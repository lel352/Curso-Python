from atexit import register
from django.template import Library
from utils import utils

register = Library()

@register.filter
def formata_preco(valor):
    return utils.formata_preco(valor)

@register.filter
def cart_total_qtd(carrinho):
    return utils.cart_total_qtd(carrinho)

@register.filter
def cart_totals(carrinho):
    return utils.cart_totals(carrinho)