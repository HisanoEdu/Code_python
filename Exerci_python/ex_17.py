#Implemente uma função encontra_palavra(texto,palavra) que retorne o índice da primeira ocorrência de uma 
#palavra em uma string.

def encontra_palavra(texto,palavra):
    indice=texto.find(palavra)
    return indice

texto="Gosto de mim, mas não é confortavel ser eu 'Rita Lee'."
palavra="Rita Lee"
indice=encontra_palavra(texto,palavra)

if indice !=1:
    print("Rita Lee '{palavra}' foi encontrada no {indice}.")
else:
    print("Rita Lee '{palavra}'não foi encontrada no texto")