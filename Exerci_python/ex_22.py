#Escreva uma função maior_elemento(lista) que retorne o maior número de uma lista.

def maior_elemento(lista):

    if not lista:
        return None 
    
    maior = max(lista)
    
    return maior

if __name__ == "__main__":
    
    lista = [10, 20, 5, 30, 25]
    
    resultado = maior_elemento(lista)
    
    # Exibe o resultado
    print("Lista:", lista)
    print("Maior elemento:", resultado)
