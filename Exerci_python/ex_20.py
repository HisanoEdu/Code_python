#Implemente uma função troca_vogais(s,nova_letra) que substitua todas as vogais de 
# string por uma nova letra.

def troca_vogais(s, nova_letra):
    
    vogais = "aeiouAEIOU"
    
    nova_string = ''.join([nova_letra if char in vogais else char for char in s])
    
    return nova_string


if __name__ == "__main__":
    
    s = "Um belo dia resolvi mudar e fazer tudo que queria fazer, me libertei daquela vida vulgar (Rita Lee)"
    nova_letra = "*"
    
    resultado = troca_vogais(s, nova_letra)
    
    print("String original:", s)
    print("String com vogais trocadas:", resultado)
