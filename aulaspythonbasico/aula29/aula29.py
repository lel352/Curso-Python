
secreto = 'python'

for letra_secreta in secreto:
    if letra_secreta != 't':
        print(letra_secreta)


secreto_temporario = ''
digitadas = []

for letra_secreta in secreto: # iteração
     if letra_secreta in digitadas:
         secreto_temporario += letra_secreta
     else:
         secreto_temporario += '*'



