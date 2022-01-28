from django import template

register = template.Library()

@register.filter(name='plural_comentarios')
def plural_comentarios(numero_comentarios):
    try:
        numero_comentarios = int(numero_comentarios)
        if numero_comentarios == 0:
            return f'Nenhum Comentário'
        elif numero_comentarios == 1:
            return f'{numero_comentarios} Comentário'
        else:
            return f'{numero_comentarios} Comentários'
    except:
        return f'{numero_comentarios} Comentário(s)'


