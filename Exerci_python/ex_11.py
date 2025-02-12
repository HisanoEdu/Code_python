#Crie uma função conta_palavras(texto) que conte quantas palavras existem em uma string

def conta_palavras(texto):
    palavras = texto.split()
    
    return len(palavras)

texto1 = "Olá, como você está?"
resultado1 = conta_palavras(texto1)
print(f'Número de palavras no texto "{texto1}": {resultado1}')
