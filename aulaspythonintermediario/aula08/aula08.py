perguntas  = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '8'
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2?',
        'respostas': {
            'a': '4',
            'b': '10',
            'c': '6'
        },
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 1+2?',
        'respostas': {
            'a': '3',
            'b': '10',
            'c': '6'
        },
        'resposta_certa': 'a',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 1-1?',
        'respostas': {
            'a': '2',
            'b': '1',
            'c': '0'
        },
        'resposta_certa': 'c',
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 8/4?',
        'respostas': {
            'a': '0',
            'b': '4',
            'c': '2'
        },
        'resposta_certa': 'c',
    },
}
resposta_certa = 0

for pk, pv in perguntas.items():
    print(f'{pk}:{pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta = input('Sua resposta: ')
    if resposta == pv['resposta_certa']:
        print('Você Acertou !!!')
        resposta_certa += 1
    else:
        print('Você Errou !!!')

    print()

qtd_perguntas = len(perguntas)
por_acerto = resposta_certa / qtd_perguntas * 100
print(f'Você acertou {resposta_certa} pergunta(s). ')
print(f'Sua porcetagem de acerto foi de {por_acerto:.2f}%.')