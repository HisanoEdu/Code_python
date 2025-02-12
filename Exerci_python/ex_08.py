#08)implemente uma função inverte_string(s) que retorne a string s invertida.

def inverte_string(s):
    return s[::-1]  


texto1 = "Python"
resultado1 = inverte_string(texto1)
print(f'String invertida de "{texto1}": {resultado1}')  


texto2 = "Eu amo programar"
resultado2 = inverte_string(texto2)
print(f'String invertida de "{texto2}": {resultado2}')  


texto3 = ""
resultado3 = inverte_string(texto3)
print(f'String invertida de "{texto3}": {resultado3}')  
