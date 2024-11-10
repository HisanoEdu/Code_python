#Crie uma função apaga_vogais(s) que remova todas as vogais de uma string.

def apaga_vogais(s):
    
    vogais = "aeiouAEIOU"
    
    nova_string = ''.join([char for char in s if char not in vogais])
    
    return nova_string

if __name__ == "__main__":
    
    s = "Deus, me protega da sua macumba, Deus me salve da sua praga"
    
    resultado = apaga_vogais(s)
    
    print("String original:", s)
    print("String sem vogais:", resultado)
