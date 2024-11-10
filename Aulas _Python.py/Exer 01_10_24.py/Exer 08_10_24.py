#Atividade


#1 Escreva um programa para ler 2 valores (considere que não serão informado valores iguais ) e escrever o maior deles.

x=("Digite o primeiro valor ")
y=("Digite o segundo valor ")

if x>y:
     print("O valor maior é x")
else:
     print("O valor maior é y")



#2 Escreva um progrma para ler o ano de nascimento de uma pessoa
# e escrever uma mensagem que diga se ela poderá ou não votar este ano
#(não é necessário considerar o mês em que ela nasceu).

Ano_atual=2024
Ano=int(input("Digite o seu ano de nascimento "))
idade=Ano_atual-Ano
if Ano>=16:
    print("Pode votar")
else:
      print("Não pode votar")

#3 Escreva um programa que verifique a validade de uma senha
#senha fornecida pelo usuário. A senha validade é numero 1234.
#Devem ser impressas as seguintes mensagens:Acesso permitido caso a senha seja válida.
#Acesso negado caso a senha seja inválida.

senha=int(input("Digite sua senha "))
if senha==1234:
     print("Senha válida")
else:
      print("Senha inválida")

#4 As maçãs custam R$ 0,30 cada se forem compradas menos do que uma duzia,
#e R$ 0,25 se forem compradas pelo menos doze. Escreva um programa que leia o numero
# de maçãs compradas, calcule e escreva o valor total da compra.

maca=float(input("Escreva quantas maçãs foram compradas "))
if maca <12:
     x=maca*0.30
     print(x)
elif maca>=12:
     x=maca*0.25
     print("O valor total" , x)

#5 Escreva um programa para ler 3 valores inteiros
#(considere que não serão lidos valores iguias) e escrevê-los em ordem crescente.

a= float(input("Digite um nùmeros "))
b= float(input("Digite um nùmeros "))
c= float(input("Digite um nùmeros "))

if a<b and c<b:
     print(a,b,c)
elif a<c and c<b:
     print(a,c,b)
elif b<a and a<c:
     print(b,a,c)
elif b<c and c<a:
     print(b,c,a)
elif c<a and a<b:
     print(a,b,c)
elif c<b and b<a:
     print(c,b,a)



     
   




     






