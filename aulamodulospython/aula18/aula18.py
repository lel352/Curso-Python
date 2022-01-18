from time import sleep
from threading import Thread, Lock


'''
class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):  # sobreescrevendo
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread('Thread 1', 5)
t1.start()

t2 = MeuThread('Thread 2', 3)
t2.start()

t3 = MeuThread('Thread 3', 2)
t3.start()

for i in range(10):
    print(i)
    sleep(1)

'''

'''
print('*' * 25)


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo! 1', 5))
t1.start()

t2 = Thread(target=vai_demorar, args=('Olá mundo! 2', 1))
t2.start()

t3 = Thread(target=vai_demorar, args=('Olá mundo! 3', 2))
t3.start()

for i in range(10):
    print(i)
    sleep(.5)


'''
'''
print('*' * 25)


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

t1 = Thread(target=vai_demorar, args=('Olá mundo! 1', 10))
t1.start()

while t1.is_alive(): # Esperando a Thread terminar
    print('Esperando a Thread.')
    sleep(2)

print('Thread Acabou.')

print('*' * 25)

t1 = Thread(target=vai_demorar, args=('Olá mundo! 1', 10))
t1.start()
t1.join() # Aqui fica esperando a Thread acabar para continuar executando o código.

print('Thread Acabou.')

print('*' * 25)
'''

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()  # para problemas em usar Thread

    def comprar(self, quantidade):
        self.lock.acquire() # Bloquear para uma só thread por vez
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release()  # Desbloquear
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). Ainda temos {self.estoque} em estoques')
        self.lock.release()  # Desbloquear

if __name__ == '__main__':
    ingressos = Ingressos(10)
    threads = []
    for i in range(1, 10):
        t = Thread(target=ingressos.comprar, args=(i,))  # colocar uma vigura pq é uma tupla
        threads.append(t)
        # t.start()

    for t in threads:
        t.start()

    executando = True
    while executando:
        executando = False
        for t in threads:
            if t.is_alive():
                executando = True
                break

    print(ingressos.estoque)
