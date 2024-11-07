#Funções no python

#São bloco de código

def hello():
    print("Olá")

# Como chamar uma função é o mesmo de chamar um apessoa pelo nome.

#Basta escrever o nome delae, ela roda.

#Vai rodar linha por linha até encontrar o nome, o python pula esse def.

#função (hello()) - nome  chamamos de nome()
#def nome()

#paramentro é uma variavel que vai receber ums string

def hello(nome):
    print("Olá", nome)
hello("Eduarda")


def nanami (nome):
    print("Olá",nome)
nanami("Eduarda")


#obs no lugar de hello pode colocar qualquer nome.

#Essa função de nome hello tem como objetivo imprimir o Óla.

def hello(nome):
 print("Seja Bem-vindo",nome)

a=input("Digite seu nome = ")
hello(a)


def hello(Luffy):
 print("Seja Bem-vindo",Luffy)

a=input("Digite seu nome = ")
hello(a)

nome=input("Digite seu nome ")
idade=input("Digite sua idade")
hello(nome,idade)


def hello(nome, idade):
  print("Olá",nome,'\nSua idade é:', idade)
hello("Eduarda",23)

# função de cálculo pagamento

def calcular_pagamento(qtd_horas,valor_horas):
    horas=float(qtd_horas)
    taxa=float(valor_horas)
    if horas<=40:
       salario=horas*taxa
    else:
       h_excd=horas-40
       salario=40*taxa+(h_excd*(1.5*taxa))
       print(salario)



def calcular_pagamento(qtd_horas,valor_horas):
    print(qtd_horas,valor_horas)

x=float(input("Digite a quantidade de horas trabalhada "))
y=float(input("Digite o valor de horas trabalhada "))

horas=float(x)
taxa=float(y)
if horas<=40:
    salario=horas*taxa
else:
       h_excd=horas-40
       salario=40*taxa+(h_excd*(1.5*taxa))
       print(salario)


# #Função de return, fazer tarefas especificas de preferencia da amaneira mais clara 
# #mandar retornar o conteudo da variavel, do valor, expressão ou objeto

def soma(x,y):
  result=x,y
  #return result  

a=int(input("Primeiro numero: "))
b=int(input("Segundo numero: "))
res=soma(a,b)#atribua a uma variável
print("soma:",res)


def soma(x,y):
    result=x+y
    return result
a=int(input("Primeiro numero: "))
b=int(input("Segundo numero: "))
res=soma(a,b)
print("Soma",res)

def inverte(nome,sobrenome):
    nomeinverso=sobrenome+","+nome
    return nomeinverso
nome=input("nome:")
sobrenome=input("Sobrenome")
invertido=inverte(nome,sobrenome)
print("Olá",invertido)

#Função booleano
#Return true and false

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

# def cadastro():
#     name=input("Qual seu nome:")
#     age=int(input("Idade"))
#     return name,age

#     print("Iniciando cadastro...")
#     nome,Idade=cadastro()
#     print("Cadastro realizado com sucesso:")
#     print("Seu nome é,"nome" e você tem,"Idade" anos de idade)
         
