# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os


def cabecalho():
    print('Comandos: listar, desfazer e refazer')
    return input('Digite uma tarefa ou comando: ')


def lista_vazia(lista):
    if not lista:
        return True
    return False


def listar(lista):
    print(' ')
    print('TAREFAS: ')
    if lista_vazia(lista):
        print('SEM TAREFAS')
        print(' ')
        return

    for l in lista:
        print(f' - {l}')
    print(' ')


def adicionar(acao, lista):
    print()
    acao = acao.strip()
    if not acao:
        print('Você não digitou uma tarefa.')
        return
    print(f'{acao=} adicionada na lista de tarefas.')
    lista.append(acao)
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if lista_vazia(tarefas):
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if lista_vazia(tarefas_refazer):
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


def analisar_comando(comando, tarefas, tarefas_refazer):
    acao = comando
    acao = acao.lower().strip()
    if acao == 'listar':
        listar(tarefas)
    elif acao == 'clear':
        os.system('clear')
    elif acao == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
    elif acao == 'refazer':
        refazer(tarefas, tarefas_refazer)
    else:
        adicionar(acao, tarefas)
        listar(tarefas)


continuar = True
tarefas = []
tarefas_refazer = []
while continuar:
    entrada = cabecalho()
    analisar_comando(entrada, tarefas, tarefas_refazer)
