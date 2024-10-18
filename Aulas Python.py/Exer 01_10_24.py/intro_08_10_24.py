#Python-tuplas
#Diferente de listas,as tuplas uma vez criadas, não permitem mudar o conteúdo uma tupla, ( ) e uma lista [ ].

#tupla index
#empresas=("Brasil" , "EUA" , "França" , "Japão")
#print(empresas.index("Japão"))

#Listas para tuplas:

#li=[[1,2],[3],[4,5,6]]
#print(type(li))

#li=(tuple(li))
#print(type(li))

#tuplas para tuplas (Tuplas x Listas)

#tu=(1,2,3,4,5,6,'a','b','c')
#print(type(tu))

#tu=(list(tu))
#print(type(tu))

#Python-Operadores relacionais

#x>y e y<x 
#x-y ou x-=y 
#x** ou x**=y
#x=x+y ou x+=y
#x%y ou x%=y

#EX: X=0 AND Y=1 "E"
#X=0 OR Y=1 "OU"

#X=1
#(x>0) and (x<100)
#Verdadeiro Pois 1 é maior que 0, ao mesmo tempo 1 é menor que 100.

#x=7
#(x==7) or (x==100)
#verdadeiro.

#Intentação são blocos definidos usa : em vez {}

x=100
if x > 0:
    print("X maior que 0")
    print("termino")
 #True

#Dar o espaço 4 para frente.

x=-1
if x <0:
    print("x é maior que 0 ")
    print("Termino")
#False

#O camando if (Significa "se")

#Vai executar o programa só se for verdade.

#else (Se não)

idade=18
if idade < 20:
    print('Você é jovem')

Age=18
if(Age>17):
    print("Você é maior,já pode dirigir")
    
idade=int(input("Digite sua idade "))
if idade >=18:#caso verdadeiro
    print("Maior de idade ")
else: #caso falso
    print("Menor de idade")


idade=int(input('Digite sua idade '))
if idade ==16: #caso verdadeiro
    print("Pode votar")
else:
    if idade>=16:
        print("Você pode dirigir")
    else:
        if idade>=16:
           print("tenta numa próxima")

#elif (Se existir mais de uma condição alternativa que precisa ser verifacada, pode utilizar o elif e avaliar as expreções ) 
#Seria um else if (Senão se)

idade=int(input("Digite sua idade "))
if idade >=16 and idade<18: #caso verdadeiro
    print("pode votar")
elif idade:
    print("Apenas estude")
else:
    print("Pode dirigir")
