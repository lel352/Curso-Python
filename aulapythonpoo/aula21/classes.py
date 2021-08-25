""" Descrição rápida e simples - Documentação referente ao módulo

What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard
dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen
book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially
unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more
 recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

Why do we use it?
It is a long established fact that a reader will be distracted by the readable content of a page when looking at its
layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using
'Content here, content here', making it look like readable English. Many desktop publishing packages and web page
editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites
still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose
(injected humour and the like).
"""

class MinhaClasse:
    """ Documentação Normal

    Conforme qualquer outra documentação que você tenha usado anteriormente.
    """

    atributo = 1
    atributo2 = 'Valor'

    def __init__(self, texto):
        """ Inicializa dos dados

        :param texto: o texto da classe
        :type texto: str
        """

        self.texto = texto
        self.exibe_texto(texto)

    @staticmethod
    def exibe_texto(texto):
        """ Método que exibe um texto de 100 caracteres na tela

        :param texto: Um texto de 100 caracteres
        :type texto: str

        :return O texto de 100 caracteres
        :rtype: Str

        :raises: ValueError: Se o texto tiver mais que 100 caracteres
        :raises: TypeError: Se o texto não for uma string
        """

        if not isinstance(texto, str):
            raise TypeError('Texto precisa ser uma string.')

        if len(texto) > 100:
            raise ValueError('Texto precisa ter 100 caracteres ou menos.')

        return texto