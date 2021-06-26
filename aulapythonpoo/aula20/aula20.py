"""
Em python tudo é um objeto: Incluindo Classes
Metaclasses são as "Classes" que criam classes.
Type é uma metaclasse (!!!???)
"""
class Meta(type):
    def __new__(mcs, name, bass, namespace):
        if name in 'A,C':
            return type.__new__(mcs, name, bass, namespace)

        if 'b_fala' not in namespace:
           print(f"oi, você precisa crar um método 'b_fala' em {name}")
        else:
            if not callable(namespace['b_fala']):
                print(f"oi, você precisa crar um método 'b_fala' em {name}")

        if 'attr_classe' in namespace:
            print(f"`{name} tentou sobrescrever o atributo")
            del namespace['attr_classe']  # apagando atributos na filha para impedir sobrescrever

        return type.__new__(mcs, name, bass, namespace)


# class é uma metaclasse que cria uma Classe
class A(metaclass=Meta):  # Classe
    attr = 'Valor'
    b_fala = '*'

    def fala(self):
        self.b_fala()


class B(A):
    teste = 'Valor'
    b_fala = '*'

    def b_fala(self):
        print('oi')


# instância da classe
a = A()

print('*'*25)


class C(metaclass=Meta):
    attr_classe = 'Valor C'


class D(C):
    attr_classe = 'Valor D'


d = D()
print('*'*25)
print(d.attr_classe)

print('*'*25)


class Pai:
    nome = 'Teste'


E = type('E',  # nome da classe
         (Pai,),  # quem herda
         {
             'attr': 'Olá Mundo!'
         }
)


e = E()
print(e.attr)
print(e.nome)
print(type(e))

