#Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
#descrito, exiba a saudação apropriada. Ex. 
#Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

hora = int(input("Digite que horas são: "))
tarde = hora >= 12 and hora <= 17
dia = hora <= 11 and hora >= 0
noite = hora <= 23 and hora >= 18

if dia:
    print("Bom dia")
elif tarde:
    print("Boa tarde") 
elif noite:
    print("Boa noite")
