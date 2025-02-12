#Python - Listas mutáveis.

frutas = ["Banana" , "maça" , "cereja"]
frutas[0] = "pera"
frutas[-1]= "laranja"
print (frutas)

uma_lista = ['a' , 'b' ,'c','d','e','f']
uma_lista[1:3] = ['x' , 'y']
print(uma_lista)

uma_lista= ['a' , 'b' , 'c' , 'd' , 'e' ,'f']
print(uma_lista)
print(len(uma_lista))

uma_lista[1:3]=[]
print(uma_lista)
print(len(uma_lista))

uma_lista=['a','b','f']
uma_lista[1:1]=['b','c']
print(uma_lista)
uma_lista[4:4] =['e']
print(uma_lista)

#Remover uma lista de forma mais simples.
a=['um','dois','três']
del a[1]
print(a)

lista=['a', 'b' ,'c' ,'d' ,'e','f']
del lista[1:5]
print(lista)

#Operador . (ponto) -append
#lista.comando(atributo) Ele adiciona elementos no final da lista

a=[81,82,83]
a.append(5)
print(a)

# Sort é ordenar um valor de uma lista, ordena os valores em ordem.

a=[88,81,82,83]
a.sort()
print(a)

a=[88,81,82,83]
a=lista.sort(reverse=True)
print(a)

a=[1,2,3,4,5,6,7,8,9]
print(a.index(4))
#Ele vai mostrar a posição em que o quatro está por exemplo ele esta na posição três.

#insert precisa informar onde quer adicionar na posição, insere o valor na posição desejada.

a=[88,81,82,83]
a.insert(1,100) #Posição insira 100
print(a)

#count quero contar qunatas vezes apareceu um nome na lista por exemplo ele vai contar.

a=[88,81,82,83,88,85,88,86]
print(a)
print(a.count(88))

#a.pop ele remove a posição em que você quer remover da lista

a=[88,81,82,83,88,85,88,86]
a.pop()
print(a)

a.pop(0)
print(a)

#extend acresenta os elementos de uma lista ao final da lista mais de um item.

lista=[1,2]
lista.extend([3,4])
print(lista)