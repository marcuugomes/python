#Exercicio 1

decimal = input("Introduza o número decimal: ")
aux=0
aux=int(decimal)
binario=""


while aux >0:
    if aux%2==0:
        binario+="0"
        aux=aux/2
        print(aux)
    else:
        binario+="1"
        aux=round(aux/2,0)
        print(aux)
        
print(binario)