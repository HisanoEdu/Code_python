#06) Escreva uma função soma_lista(lista) que receba uma lista de numeros e retorne a soma
# de todos os elementos

def soma_lista(lista):
    soma = 0
    for numero in lista:
        soma += numero  
    return soma

resultado = soma_lista([])
print(resultado)

resul = soma_lista([1, 2, 3, 4, 5])
print(resul)

result=soma_lista([-1,-2,-3,-4,-5])
print(resul)

