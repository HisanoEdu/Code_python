#01) Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50

for x in range(1,50,2):
    print(x)

#02) Faça um programa que imprima uma lista de times, adicionando um numeral. 
#EX:
#ENTRADA:
#Time=["Palmeiras", "Curitiba","São Paulo"]

#Saída:
#1-Palmeiras
#2-Curitiba
#3-São Paulo

time=["1-Palmeiras" , "2-Curitiba" , "3-São Paulo"]
for a in time:
    print(a)

time=["1-Palmeiras" , "2-Curitiba" , "3-São Paulo"]
for n in time:
    print(n)

#03) Faça um programa que receba dois números inteiros 
# e gere os números inteiros que estão no intervalo 
#compreendido por eles.

nume1=int(input("Digite um número: "))
nume2=int(input("Digite outro número: "))
for x in range(nume1,nume2):
    cont=cont+1 #Contador é cont
    print(x)
    
#04) Altere o programa anterior para mostrar no final a soma dos números
cont=0
soma=0
nume1=int(input("Digite um número: "))
nume2=int(input("Digite outro número: "))
for x in range(nume1+1,nume2):
    cont=cont+1 #Contador é cont
    print(x)
    soma=soma+x #acumulador é soma
print (soma)

#05) Faça um programa que imprima na tela os números de 1 a 20, 
# um abaixo do outro. Depois modifique o programa para que ele 
# mostre os numeros um ao lado do outro.


for x in range(1,21):
    print(x, end=" ") #end é para colocar os numeros lado a lado


#06)Faça um programa que leia 5 números e informe a soma e a média dos números.

cont=0
soma=0

for x in range(5):
    n=int(input("Digite 1° número: "))
    cont=cont+1
    soma=soma+n    
print(soma)

media=soma/cont
print(media)

#07) A séria de Fibonacci é formada pela sequência 
#0,1,1,2,3,5,8,13,21,34,55,...Faça um programa capaz
#de gerar a serie até o n-ésimo termo.

n=0
n1=1

fibo=int(input("Digite um número "))
n,n1=0,1
for i in range(2,fibo+1):
    n3=n+n1
    print(n3,end= " ")
    n=n1
    n1=n3


#Fibonacci exemplo
#1+1=2
#1+2=3
#2+3=5
#3+5=8
#3+8=11
#(...)
