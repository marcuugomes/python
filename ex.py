#Exercícios introdutórios à sintaxe da linguagem Python

#Exercicio 1

"""
#Input do número máximo e do número mínimo
minimo = int(input("Introduza o nº mínimo: "))
maximo = int(input("Introduza o nº máximo: "))

#Ciclo 'while' p/ percorrer do minimo ao maximo
while minimo <= maximo :
    
    if (minimo % 2) == 0:
        txt = "par!"      
    else:
        txt = "impar!"
       
    # Criar uma string que recebe o numero atual e uma string c/ o resultado    
    preset = 'O {} é {}'.format(minimo, txt)
    
    #output do resultado e acrescentar 1 ao numero minimo
    print(preset)
    minimo += 1
    
 """   
    
#Exercicio 2

#Input do numero
"""
numero = int(input("Introduza o número"))
numero2 = 1

while numero2 < 11:
    
    resultado = numero*numero2
    preset = '{} x {} = {}'.format(numero, numero2, resultado)
    print(preset)
    numero2 += 1
    
"""
    
    
#Exercicio 3
"""
#Input dos numeros
minimo = int(input("Introduza o 1º número: "))
maximo = int(input("Introduza o 2º número: "))

#Validacao
while minimo <= maximo:
        
    total = 0
    listanumero = [0]
    preset = 'O {} é primo'
    
    if minimo!=1:
            
        if minimo == 2 or minimo == 3 or minimo == 5 or minimo == 7:
            preset=preset.format(minimo)
            print(preset)
        else:
            for n in str(minimo): # percorrer cada digito do numero
                listanumero.append(int(n)) # guardar numa lista cada digito
                total = total + int(n) # somar cada digito e guardar numa variavel
            if (minimo%2)!=0 and (total%3)!=0 and (minimo%7)!=0 and listanumero[-1]!=0 and listanumero[-1]!=5 :
                preset=preset.format(minimo)
                print(preset)
            
    minimo += 1
""" 
#Exercicio 4
# Escreva um programa que calcule a capicua de um número, isto é, inverta a ordem dos
# algarismos que constituem esse número.
"""
from tkinter import N


number = int (input("Introduza o número: "))

#Converter o numero p/ uma lista com cada digitio individualmente
# Variavel lista
numberlist=[]

#Ciclo p/ percorrer cada digito e guardar numa lista
for n in str(number):
    numberlist.append(int(n))
    
string=''

for n in numberlist[::-1]:
    string=string+str(n)
    
print("A capicua do número {} é : {}".format(number, string))
"""

#Exercicio 5
#Escreva uma função que remova espaços, capitalize todas as palavras, e no final devolva
#numa lista (list) a frase decomposta por palavras. 
"""
string = input("Introduza a frase: ")      
newString=""
listaPalavras=[]

for c in string:
    if c !=" ":
        newString += c.upper()
    if c ==" " or c==string[-1]:
        listaPalavras.append(newString)
        newString=""
        
print(listaPalavras)
"""      
#Exercicio 6 
"""
nome = input("Introduza o nome: ")
aux=""
nomeSeparado=[]

for letra in nome:
    if letra!=" ":
        aux+=letra
    if letra == " " or letra==nome[-1]:
        nomeSeparado.append(aux)
        aux=" "
        
nomeFinal=nomeSeparado[-1]+","

for palavra in nomeSeparado:
    if palavra != nomeSeparado[-1]:
        nomeFinal+=" " + palavra[0].upper() + "."
        
print("O nome convertido é: " + nomeFinal)
"""

# Exercicio7
"""
palavra = input("Introduza a palavra: ")
aux =""
palavraRepetida=""
for letra in palavra:
    if letra != " ":
        aux+=letra
    if letra == " " or letra == palavra[-1]:
        palavraRepetida=aux+" "
        
i=0

while i<=5:
    print(palavraRepetida*i)
    i+=1
"""

#Exercio 8
"""
nRomano=int(input("Introduza o número (Numeração Romana) :"))
nSeparado=[]


def calcularValor (numero):
    
    for digito in numero:
        if digito =="c" or "C":
            total+=100
        if digito =="d" or "D":
            total+=500
        if digito =="m" or "M":
            total+=1000
        if digito ==
    
calcularValor()
"""
    
    





#Exercio 9
"""
import random

def generar ():
    i=0
    aux=0
    listaNumeros=[]
    count=0
    soma=0
    
    while i<20:
        listaNumeros.append(random.randint(-100,100))
        i+=1
        
    print("A lista é: ")
    print(listaNumeros)
    
    for numero in listaNumeros:
        if numero >0:
            soma+=numero
        if numero <0:
            count+=1
    print("\n")
    print("A soma dos positivos é: ",soma)
    print("Existem {} números negativos na lista".format(count))
    
    
generar()
"""