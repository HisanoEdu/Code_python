#02)Crie uma função maior(a,b) que receba dois números e retorne o maior entre eles.

def maior(a, b):
    if a > b:
        return a
    else:
        return b

while True:
    num=int(input("Insira um número:"))
    if maior(num):
     print("É par")
    else:
     print("É impar")