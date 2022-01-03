from django.contrib import admin
from .models import Categoria, Contato

class ContatoAdim(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')
    # list_filter = ('nome', 'sobrenome')
    list_per_page = 10  # somente 10 elementos por página.
    search_fields = ('nome', 'sobrenome', 'telefone')
    list_editable = ('telefone', 'mostrar')



# Register your models here.
admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdim)
