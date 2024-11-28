
from conta import conta  
# nome,cpf,saldo,senha


while True:
    tipo=int(input("1 - cadastro"))

    if tipo == 1:
        nome = input("Digite seu nome: ")
        cpf=input("Digite seu CPF: ")
        saldo=input("Digite seu saldo ")
        senha=int(input("Digite sua senha: "))


        x = conta(nome, 123,0,123)


# ex primeiro from (nome do arquivo que esta o codigo) ex: Conta_bancaria
# import é o nome da classe ex: conta


