"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    input <- Nova tarefa
"""

if __name__ == '__main__':
  to_do = []
  re_do = []


def add(to_do):
    print('*' * 25)
    print('  Adicionar Tarefa  ')
    tarefa = input('Tarefa: ')
    add_todo(to_do, tarefa)


def add_todo(to_do, tarefa):
    to_do.append(tarefa)


def do_undo(to_do, re_do):
    if not to_do:
        print('Nada a desfazer')
        return

    last_todo = to_do.pop()
    re_do.append(last_todo)

def do_redo(to_do, re_do):
    if not re_do:
        print('Nada a refazer')
        return

    last_redo = re_do.pop()
    to_do.append(last_redo)


def show_todo(to_do):
    print('*' * 25)
    print('Tarefa: ')
    print(to_do)
    print()


while True:
    print('*' * 25)
    print('  Menu  ')
    print(' 1 - Tarefa')
    print(' 2 - Desfazer ')
    print(' 3 - Refazer ')
    print(' 4 - Mostrar Lista')
    op = input(' Opção: ')
    try:
        op = int(op)
        if op == 1:
            add(to_do)
        elif op == 2:
            do_undo(to_do, re_do)
        elif op == 3:
            do_redo(to_do, re_do)
        elif op == 4:
            show_todo(to_do)
        else:
            print('Digite uma opção válida !!!')
    except Exception as erro:
        print('Digite uma opção válida !!!')
