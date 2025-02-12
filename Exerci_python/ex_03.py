#03) Escreva uma função eh_par(numero) que receba um número e retorne true se ele for par e false caso contrario.

def par(x):
    if(x%2)==0:
        return True
    else:
        return False
    
while True:
    num=int(input("Insira um número:"))
    if par(num):
     print("É par")
    else:
     print("É impar")