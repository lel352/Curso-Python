""
"""
Associação - uma classe se relaciona com outra, mas nenhuma da duas classes dependende de uma da outra
             vivem uma sem a outra 
"""

from aulapythonpoo.aula07.classes import Escritor
from aulapythonpoo.aula07.classes import Caneta
from aulapythonpoo.aula07.classes import MaquinaDeEscrever


escritor = Escritor('Joãozinho')
print(escritor.nome)

caneta = Caneta('Big')
print(caneta.marca)

maquina = MaquinaDeEscrever()
print(maquina)

escritor.ferramenta = caneta # Associação mais fraca.
escritor.ferramenta.escrever()


escritor.ferramenta = maquina
escritor.ferramenta.escrever()

# Associação mais fraca, mesmo apagando o escritor a caneta e máquina continua existindo.
del escritor
