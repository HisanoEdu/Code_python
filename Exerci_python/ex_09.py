#09) Escreva uma função fatorial(n) que calcule o fatorial de um número inteiro n.


def fatorial(n):
    
    if n == 0 or n == 1:
        return 1
    
    else:
        return n * fatorial(n - 1)


120 = fatorial(5)
print('O fatorial de 5 é: {120}') 

1 = fatorial(0)
print('O fatorial de 0 é: {1}')  


5040 = fatorial(7)
print('O fatorial de 7 é: {5040}')  
