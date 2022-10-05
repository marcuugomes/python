#Exercicio 1

"""

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

"""

#Exercicio 2 
#Escreva um programa que dada um quantia introduzida, calcula o troco devolvendo
#o menor número de notas e moedas possíveis.
#Por exemplo: 418,35€ - 2 notas de 200€; 1 nota de 10€; 1 nota de 5€; 1 moeda de 2€;
#1 moeda de 1€; 1 moeda de 0,20€; 1 moeda, de 0,10€; 1 moeda de 0,05€.

"""
quantia = float(input("Introduza a quantia: "))
troco="\n"
notas=0
moedas=0
presetnotas='{} nota(s) de {}€ \n'
presetmoedas='{} moeda(s) de {}€ \n'

if quantia-500>=0:
    while quantia-500>=0:
        quantia-=500
        notas+=1
    
    troco+=presetnotas.format(notas,500)
    notas=0

if quantia-200>=0:
    while quantia-200>=0:
        quantia-=200
        notas+=1
    
    troco+=presetnotas.format(notas,200)
    notas=0

if quantia-100>=0:
    while quantia-100>=0:
        quantia-=100
        notas+=1
    troco+=presetnotas.format(notas,100)
    notas=0
    
if quantia-50>=0:
    while quantia-50>=0:
        quantia-=50
        notas+=1
    troco+=presetnotas.format(notas,50)
    notas=0
    
if quantia-20>=0:
    while quantia-20>=0:
        quantia-=20
        notas+=1
    troco+=presetnotas.format(notas,20)
    notas=0
    
if quantia-10>=0:
    while quantia-10>=0:
        quantia-=10
        notas+=1
    troco+=presetnotas.format(notas,10)
    notas=0
    
if quantia-5>=0:
    while quantia-5>=0:
        quantia-=5
        notas+=1
    troco+=presetnotas.format(notas,5)
    notas=0
    
if quantia-2>=0:
    while quantia-2>=0:
        quantia-=2
        moedas+=1
    troco+=presetmoedas.format(moedas,2)
    moedas=0

if quantia-1>=0:
    while quantia-1>=0:
        quantia-=1
        moedas+=1
    troco+=presetmoedas.format(moedas,1)
    
print(troco)
print(quantia)

""" 

#Exercicio 3

def comparar ():
    i=0
 

