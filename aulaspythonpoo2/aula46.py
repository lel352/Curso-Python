# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    # def __call__(self, *args, **kwds):
    def __call__(self, nome):
        print(nome, 'está Chamando', self.phone)
        return True


call1 = CallMe('321312312312312')
call1('Peter Paker')
