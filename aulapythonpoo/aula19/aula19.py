"""
Animal -> Respirar (é um Animal)
    Lobo(Animal)  -> Respirar / uivar - (lobo é um Lobo e um Animal)
        cachorro(Lobo)  -> Respirar / uivar / Latir - (Cachorro é um Cachorrp, um Lobo e um Animal)
Herança vem de cima para baixo.
"""

"""
Biblioteca
    Interface(Biblioteca)
        metodo_da_interface
"""

from aulapythonpoo.aula19.classes.interface import InterFace

i1 = InterFace()
i1.metodo_da_interface()
i1.chama_metodo_da_interface()