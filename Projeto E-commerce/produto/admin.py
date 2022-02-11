from django.contrib import admin
from produto.models import Produto, Variacao

class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 1

class ProdutoAdmin(admin.ModelAdmin):
    inlines = [
        VariacaoInline
    ]

admin.site.register(Produto)
admin.site.register(Variacao)
