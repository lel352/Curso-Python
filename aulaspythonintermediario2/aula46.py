import importlib

import aula46_m # singleton

print(aula46_m.variavel)

for i in range(10):
    importlib.reload(aula46_m)
    print(i)

print('Fim')