# For - python ao lado percorremos a lista nomes e imprimimos cada elemento.

#for n (uma variavel fazia) in nomes:

#string ex: nome="Eduarda"
#for n in nomes:
#print(n)

#lista ex: nome= "Pedro" , "João" , "leticia"

#lista
# nome=["Pedro" , "João" , "Letícia"]
# for n in nome:
#     print(n)

# # string
# nome=("Eduarda")
# for n in nome:
#     print(n)

#Break para o loop de repetição.

# nome=["Pedro" , "João" , "Letícia"]
# for n in nome:
#     print(n)
#     if n =="João":
#         break
# Com o break só vai imprimir Pedro e João e não vai imprimir Leticia.

#for continue 

# nome==["Pedro," "João" , "Letícia"]
# for n in nome:
#     if n=="João":
#         continue
#     print(n)

# No exemplo acima,quando a interação encontrar João, o algoritmo
#irá pular os passos abaixo e seguir para a próxima iteração.

# x=10

# while x>0:
#     if x==5:
#         continue
#     print(x)
#     x=x-1

# For range () percorre um conjunto de códigos um determinado número de vezes.


# for x in range(6):
#     print(x)

# retorna numa sequincias de numeros, coemçando por zero por padrão e incrementa o 1.


# for x in range(2,6):
#     print(x)

#incrementar a sequencia em 1, no entanto, é possivel especificar o 
#valor do incremento adicionando um terceiro parâmetro:

#range(2,30,3):
#início/fim/incremento

# for x in range(2,10,2):
#     print(x)

# for -loop aninhado

# for i in range(5):
#     for j in range(6):
#         print(i,j)

# for i in range(5): 0,1,2,3,4
#  for j in range(6): 0,1,2,3,4,5


#Exercios:

#01) Desenvolva uma tabuada (1 ao 10) de multiplicação com o for aninhado, não esqueça de seguir
#o padrão de impressão.

# tabu=int(input("Digite um número "))

# for x in range(11):
#     for i in range(11):
#         print(x,i)
#     print( x ,"x", i ,"=" , x*i)



# for x in range(1,11):
#     for y in range (1,11):
#         print(x, "x" , y, "=", x*y)


x=int(input("Digite um número "))
for y in range (1,11):
    print(x, "x" , y, "=", x*y)