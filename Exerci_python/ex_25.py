#Escreva uma função remove_duplicados(lista) que retorne uma lista sem elementos duplicados.

def remove_duplicados(lista):
    
    lista_sem_duplicados = list(set(lista))
    
    return lista_sem_duplicados


if __name__ == "__main__":
    lista = [1, 2, 3, 2, 4, 5, 3, 6, 7, 5]
    
    resultado = remove_duplicados(lista)
    
    print("Lista original:", lista)
    print("Lista sem duplicados:", resultado)
