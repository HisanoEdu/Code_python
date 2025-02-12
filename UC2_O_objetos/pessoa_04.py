#04) Crie uma classe que modele uma pessao:
#Atributos:nome,idade,peso e altura
#metodos: Envelhecer, engordar,emagrecer,crescer.Obs:Por padrão, 
#a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5cm.

class Pessoa():
 def __init__(self,nome,idade,peso,altura):
        self.nome=nome 
        self.idade=idade
        self.peso=peso 
        self.altura=altura

def envelhecer(self,anos):
  for ano in range(anos):
     self.idade+=1
     if self.idade < 21:
        self.crescer(0.5)

def engordar(self,quilos):
        self.peso = + quilos

def emagrecer(self,quilos):
        self.peso=-quilos
              
def crescer(self,centimentros):
    self.altura=+ centimentros

    def __str__(self):
      return f"{self.nome}, {self.idade} anos,{self.peso} kg,{self.altura} cm."

pessoa=Pessoa("Eduarda",23,50,164)
pessoa.envelhecer(2)
pessoa.emagrecer(2)
print(pessoa)