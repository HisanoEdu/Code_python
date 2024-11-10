#07) Crie uma função conta vogais (texto) que retorne o número de vogais em uma string.

def conta_vogais(texto):
    vogais = "aeiouAEIOU"  
    contador = 0  

    for char in texto:  
        if char in vogais:  
            contador += 1  

    return contador

# Testando a função
texto1 = "Olá, como você está?"
resultado1 = conta_vogais(texto1)
print(f'Número de vogais no texto "{texto1}": {resultado1}')
