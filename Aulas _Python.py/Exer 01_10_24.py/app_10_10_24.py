#App bancário

saldo=0.0
senha=1234
digite=int(input("Informe sua senha "))
if digite==senha:

    opcao=float(input("Escolha uma opção a seguir:\n1.Extrato\n2.Depósito\n3.Saque\n4.Adm\n5.Sair\n\n\n\n\n"))

    if opcao==1:
        print("Seu saldo é de " , saldo)

    elif opcao==2:
        deposito=int(input("Informe o valor do depósito "))
        saldo=saldo+deposito
        print("O seu saldo é de " , saldo)

    elif opcao==3:
        saque=int(input("Informe o valor do saque "))
        saldo=saldo-saque
        print("Seu saldo é de ", saldo)

    elif opcao==4:
        print("Nome XXX\nSexo XXX\nCPF XXX\nTelefone xxx\n ")
        nome=str(input("Digite seu nome "))
        cpf=int(input("Digite seu CPF "))
        tel=int(input("Digite seu telefone"))
        se=str(input("Digite seu sexo "))
        
        print("\n\n\nSeu nome é",nome)
        print("Seu CPF é",cpf)
        print("Seu telefone é",tel)
        print("Seu sexo é",se)

# elif opcao==5:
#     print("")

else:
        print("Senha invalida")



     

   










      
      