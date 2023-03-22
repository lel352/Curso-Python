"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'casa'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra) > 1 or letra.isdigit(): 
        print('Digite somente uma letra. ')
        continue
    
    if letra in palavra_secreta:
        letras_acertadas += letra

    acertos_palavra = ''   

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            acertos_palavra += letra_secreta
        else: 
            acertos_palavra += '*'
    
    print(f'Palavra formatada: {acertos_palavra}')

    if not '*' in acertos_palavra:
    
        os.system('cls')    
        print('VOCÊ GANHOU -  PARABÉNS !!! ')
        print(f'A palavra era: {palavra_secreta}')
        print(f'Tentativas: {numero_tentativas}')
        letras_acertadas = ''
        numero_tentativas = 0
        
    

