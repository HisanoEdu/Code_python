#Crie uma função eh_primo(n) que verifique se um número é primo.

def eh_primo(n):
    if n <= 1:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

numero = int(input("Digite um número para verificar se é primo: "))
if eh_primo(numero):
    print(f"{numero} é primo!")
else:
    print(f"{numero} não é primo.")

