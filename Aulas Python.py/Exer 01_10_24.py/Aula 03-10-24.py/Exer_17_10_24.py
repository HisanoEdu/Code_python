#Estrutura de repetição 
#python-While

#Permite que o programa ficar repetindo,varias vezes.

#podemos gerar um laço infinito com while true

# aperta primiero no terminal e depois dá um ctrl + c para parar o loop infinito.

# while True:
#     print("\nLoop infinito")

# while True:
#     valor=int(input("Digite 1 ou 0    para fim"))
#     if valor==1:
#         print("Valor correto")
#     else:
#         print("Valor para sair")
#         break

# while True:
#     valor=int(input("Digite o valor 1 ou 0      para encerrar"))
#     if valor>=1:
#         continue
#     print("maior que um")
#     if valor>=1:
#         print("maior que um")

# #Exercicio
#Algoritmo que conta quantas vezes se pode reduzir em 1 o valor
#do número passado como parâmetro até chegar a zero.
#ex:número 100

# while True:
#     nume=int(input("Digite um valor "))
#     cont=0
#     while True>=0:
#         cont=cont+1
#         nume+nume-1
#         print(cont)

#Exer Desenvolva uma calculadora que solicita qual operação desejada (Multiplicação,divisão,adição e subtração)imprima um menu.
#utilizando "While" o menu ficara ativo até que o usuário digite um comando para interromper.Verifique a partir de testes condicionais
#qual opção desejada,solicite os valores para a operação e efetue o calcule. Imprima o resultado e retorne ao menu principal.

# while True:

#     opcao=int(input("Escolha a operação desejada \n1.Multiplicação \n2.Divisão \n3.Adição \n4.Subtração \n5.Sair"))
#     print(opcao)
#     if opcao==1:
#         valor1=int(input("Digite um valor "))
#         valor2=int(input("Digite um valor "))
#         a=valor1**valor2
#         print("Multiplicação" , a)


#     if opcao==2:
#         valor1=int(input("Digite um valor "))
#         valor2=int(input("Digite um valor "))
#         b=valor1/valor2
#         print("Divisão" , b)

#     if opcao==3:
#         valor1=int(input("Digite um valor "))
#         valor2=int(input("Digite um valor "))
#         c=valor1+valor2
#         print("Adição" ,c)

#     if opcao==4:
#        valor1=int(input("Digite um valor "))
#        valor2=int(input("Digite um valor "))
#        d=valor1-valor2
#        print("Subtração",d)

#     if opcao==5:
#         print("Sair")
#         break
#     else:
    #     print("Opção invalida")
    
    # print ("\n\n")
    

#01) Faça um programa que peça uma nota, entre zero e dez.
#Mostre uma mensagem caso o valor seja invalida e continue
#pedindo até que o usuário informe um valor válido.

# while True:
#     x=int(input("Digite um valor de 0 a 10: "))

#     if x>=-1 and x<=10:
#         print(x)
#         break

#     else:
#         print("Opção invalida")


#02) Faça um programa que leia um nome de usuário e a sua senha 
#e não aceite a senha igual ao nome do usuário, mostradando uma
#mensagem de erro e voltado a pedir as informações.

# while True:
#     nome=input("Digite o seu nome: ")
#     senha=input("Digite sua senha:")
     

#     if nome==senha:
#         print("Opção invalida")

#     else:
#         print("Opção Válida")
#         break

#03) Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres
#Idade: entre 0 e 150
#salário: maior que zero
#sexo:F, M ou outro
#Estado Civil:S,c,v,divorciado

while True:
    nome=str(input("Digite o seu nome: "))

    if len(nome)>3:
        print("Valido")
        break
    else:
        print("inválido")

while True:
    idade=int(input("Digite sua idade: "))

    if idade>0 and idade<=150:
        print(idade)
        break
    else:
        print("Idade inválida")

while True:
    Salario=input("Digite seu salário")

    if Salario>0:
        print(Salario)
        break
    else:
       print("Salário inavalido")

while True:
    sexo=input("Digite seu sexo: ")

    if sexo == "F" or "M" or "O":
        print("Sexo")
        break
    else:
        print("Invalido")
    
while True:
     Estado_civil=input("Estado Civil: ")

     if Estado_civil=="S" or "C" or "V" or "D":
        print("Valido")
        break
     else:
        print("Inválido")

#Break para parar o laço que cria.

