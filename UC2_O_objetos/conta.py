
# Pilares da progrmação orientada a objeto Pilares

#Encapsulamento (foca em proteger os dados internos)
#Herança(permite compartilham  similaridade entre classes atributo e comportamento,formando uma hierarquia)
#Polomorfismo (Alterar as classes filho sem alterar a classe diferentes)
#Abstração (Refere-se a mostrar apenas os detalhes essenciais de um objeto ou classe e esconder,ocultar o necessário)

# class encapsulamento():
#     def __init__ (self,num1,num2):
#            self.__num1=num1
#            self.__num2=num2

# def adicionar(self):
#     return self.__num1+self.__num2

# calc=encapsulamento(20,10)
# print(calc.adicionar())
# calc.__num1

# exercicio

# Desenvolva um algoritmo de uma conta bancária, que deverá conter os
# seguintes itens:
# Arquivo da classe conta, terá um método construtor (__init_), com os
# seguintes parâmetros: nome(público), saldo(privado), cpf(privado) e
# senha(privado). Também conterá mais três métodos: 
# 
# método extrato(),que solicitara uma senha e fará a conferência com a senha do método
# __init_ caso seja verdadeira, mostrar o saldo, caso seja falso, imprimir
# "Senha inválida"; terá também o método depositar que receberá como
# parâmetro um valor e acrescentará ao saldo; e por último, o método
# sacar que solicitará a senha do método _init__ um valor de saque,
# caso seja verdadeira a senha, retirar do saldo, o valor solicitado, caso
# seja falso, imprimir "Senha inválida",
# ○ arquivo main conterá o menu com: cadastro, saldo, saque e depósito.

#metodos: extrato(senha)
#depositar(valor)
#sacar(senha,valor)


class conta:
    def __init__(self,nome,cpf,saldo,senha):
        self.nome=nome     
        self.__cpf=cpf
        self.__saldo=saldo
        self.__senha=senha
        print("Cadastro efetuado com sucesso")

def depositar(self,valor):
     self.saldo+= valor

def sacar(self,valor):
      self.saldo-=valor

def extrato(self,senha):
    if senha==senha.__senha:
          return f"Saldo atual: R${self.valor}"
    else:
        print("Senha inválida")

def gerar_extrato(self):
     print(f"numero:{self.numero}\n Nome: {self.nome}\n cpf: {self.cpf}\n saldo sehha:{self.senha}")
    

