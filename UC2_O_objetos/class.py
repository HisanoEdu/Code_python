
#21/11/24

#Tudo é um objeto em programação orientada a objeto.
#Pensar como se fose uma super variaval.
#metodo é uma acão.
#isntancia é um objeto (trazer um objeto a fazer algo)

class Vendedor():
    def __init__(self,nome,vendas):
        self.nome=nome 
        self.vendas=vendas

#__init__ vai iniciar a classe conhecido como Método construtor.

Vendedor1=Vendedor('Eduarda',1000)
print(Vendedor1.nome)