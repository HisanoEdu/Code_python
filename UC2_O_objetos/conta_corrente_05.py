
#05) Crie uma classe para implementar uma conta corrente.
# A classe deve possuir os seguintes atributos:número da conta, nome do correntista e saldo.
#Os metodos são o seguinte:alterar_nome,deposito e saque. 
#No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatorios.

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
       
        self.nome_correntista = novo_nome
        print(f"Nome alterado para {self.nome_correntista}")

    def deposito(self, valor):
        
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Valor de depósito inválido. O valor deve ser maior que zero.")

    def saque(self, valor):
    
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor de saque inválido. O valor deve ser maior que zero.")


conta1 = ContaCorrente(12345, "João Silva")
conta1.deposito(1000)
conta1.saque(500)
conta1.alterar_nome("João Souza")
