
#Deselvolva uma classe super que conterá dados de cadastro comuns, como nome, endereço,fone etc
# 10 dados.

class Pessoa:
    def __init__(self):
        self.nome=(input("Digite seu nome"))
        self.data_de_nascimento=(input("Qual a sua data de nascimento?"))
        self.sexo=(input("Qual é o seu sexo?"))
        self.email=(input("Digite seu email"))
        self.endereço=(input("Digite seu endereço"))
        self.cidade=(input("Digite sua cidade"))
        self.fone=(input("Digite o seu telefone"))


class PF (Pessoa):
     def PFisica(self):
         self.cpf=(input("Qual seu CPF?"))
         self.estado_civil=(input("Digite seu estdo civil"))
         self.RG=(input("Digite o seu RG"))

class Pj(Pessoa):
    def Pjuridica(self):
        self.cnpj=(input("Qual é o CNPJ da empresa?"))
        self.natureza=(input("Qual é a natureza juridica da sua empresa?"))

teste=Pessoa()
teste.PFisica()





