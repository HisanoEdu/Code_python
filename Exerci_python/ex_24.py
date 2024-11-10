# Crie uma função conta_ocorrencias(lista,elemento) que conta quantas vezes um elemento aparece em uma lista.


def conta_ocorrencias(lista, elemento):
    ocorrencias = lista.count(elemento)
    
    return ocorrencias

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 2, 5, 2, 6]
    elemento = 2
    
    resultado = conta_ocorrencias(lista, elemento)
    
    print(f"O elemento {elemento} aparece {resultado} vez(es) na lista.")
