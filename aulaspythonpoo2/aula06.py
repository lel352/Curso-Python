
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Já está filmando...')
            return

        print(f'{self.nome} está filmando...')
        self.filmando = True

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} Não pode fotografar filmando.')
            return

        print(f'{self.nome} está fotografando...')

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} Não está filmando...')
            return

        print(f'{self.nome} parou de filmar...')
        self.filmando = False


c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar()
print(c1.filmando)
print(c2.filmando)
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()
