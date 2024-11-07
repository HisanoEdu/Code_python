#Exercicios

#01) Faça um programa, com uma função que necessite de três argumentos, e que forneça
# a soma dos dois primeiros argumentos e multiplicado pelo terceiro.

def soma(x,y,z):
    result=(x+y)*z
    return result
    
a=int(input("Primeiro numero: "))
b=int(input("Segundo numero: "))
z=int(input("Terceiro numero"))
res=soma(a,b,z)

print("Soma",res)

#02) Faça um programa, com uma função que necessite de um argumento.
#A função retorna o valor de caracter "P", se seu argumento for positivo,
#e "N", se seu argumento negativo, e zero se seu argumento for 0.

  
def par(x):
    if x<0:
        return True
    else:
        return False
    
while True:
    nume=int(input("Insira um número\n1 para positivo\n-1 para negativo:"))
    if par(nume):
     print("N")
    elif nume==0:
       print("ZERO")
    else:
     print("P")

#03) Faça um programa com uma função chamada somalmposto.
#A função possui dois parâmetros formais:taxalmpostos, que
# é a quantia do imposto sobre vendas expressa em porcentagem e
# custo, que é custo de um item antes do imposto. A função "Altera"
#o valor de custo para concluir o imposto sobre vendas.

def hello(somalposto,taxalmposto):
    print(somalposto,taxalposto)

x=float(input("Digiteo valor do seu imposto"))
y=float(input(" Digite a taxa do imposto"))

horas=float(x)
taxa=float(y)
if horas<=40:
    salario=horas*taxa
else:
       h_excd=horas-40
       salario=40*taxa+(h_excd*(1.5*taxa))
       print(salario)

