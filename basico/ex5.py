nome = input("Digite seu nome:")
idade = input("Digite sua idade:")

if not idade or not nome:
    print("Desculpe, você deixou campos vazios.")

elif (" ") in nome:
    print (f"Seu nome é {nome}")
    print (f"Seu nome invertido é: {nome[::-1]}")
    print (f"Seu nome contém espaços")
    print (f"Seu nome contém: {len(nome)} letras")
    print (f"A primeira letra do seu nome é: {nome[0:1:]}")
    print (f"A ultima letra do seu nome é: {nome[-1:len(nome):1]}")

elif (" ") not in nome:
    print (f"Seu nome é {nome}")
    print (f"Seu nome invertido é: {nome[::-1]}")
    print (f"Seu nome não contém espaços")
    print (f"Seu nome contém: {len(nome)} letras")
    print (f"A primeira letra do seu nome é: {nome[0:1:]}")
    print (f"A ultima letra do seu nome é: {nome[-1:len(nome):1]}")

