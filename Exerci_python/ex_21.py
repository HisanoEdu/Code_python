# Crie uma função media_lista(lista) que receba uma lista de números e retorne a média.

def media_lista(lista):
    
    if not lista:
        return 0 
    
    soma = sum(lista)
    
    quantidade = len(lista)
    
    media = soma / quantidade
    
    return media

if __name__ == "__main__":
    
    lista = [10, 20, 30, 40, 50]
    
    resultado = media_lista(lista)
    
    
    print("Lista:", lista)
    print("Média da lista:", resultado)
