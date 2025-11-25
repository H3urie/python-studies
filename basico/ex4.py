n1 = int(input("digite a primeira nota do bimestre:"))
n2 = int(input("digite a segunda nota do bimestre:"))
n3 = int(input("digite a terceira nota do bimestre:"))
n4 = int(input("digite a quarta nota do bimestre:"))
n5 = int(input("digite a quinta nota do bimestre:"))

soma = n1+n2+n3+n4+n5
div = soma/5

print("A média das notas {}, {}, {}, {} e {} resulta em: {:.2f}".format(n1,n2,n3,n4,n5,div))

if div >= 6:
    print("VOCÊ FOI APROVADO!")
else:
    print ("VOCÊ FOI REPROVADO!")