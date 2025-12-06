#Faça um programa que peça o nome do usuário. utilizando While, adicione
#um "*" em cada letra do nome, por exemplo: *L*u*i*z *O*t*a*v*i*o*


nome = "Vinicius Oliveira"
tamanho = 0
novo_nome = ""

while tamanho < len(nome):
    letra = nome[tamanho]
    novo_nome += (f"*{letra}")
    tamanho += 1

novo_nome += "*"
print(novo_nome)