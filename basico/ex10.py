#Faça um programa que peça uma frase ao usuario e identifique a letraque apareceu
#mais vezes na frase e retorne para o usuario essa letra e a quantidade de vezes.

frase = input("Digite sua frase: ")

indice = 0
qnt_apareceu_mais = 0
letra_apareceu_mais = ""


while indice < len(frase):

    letra_atual = frase[indice]

    if letra_atual == " ":
        indice += 1
        continue

    qnt_vezes_apareceu = frase.count(letra_atual)

    
    if qnt_apareceu_mais < qnt_vezes_apareceu:
        qnt_apareceu_mais = qnt_vezes_apareceu
        letra_apareceu_mais = letra_atual


    indice += 1
   

print(f"a letra que mais aparceu em sua frase é: '{letra_apareceu_mais}' e apareceu {qnt_apareceu_mais} vezes;")