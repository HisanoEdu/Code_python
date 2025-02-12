
#02) Classe quadrado: Crie uma classe que molde um quadrado:
#Atributos:Tamanho do lado 
#metodos: Mostrar_area,mudar_valor_lado(Retornar valor do lado e calcular area)

class Quadrado():
        def __init__(self, tamanhoLado):
            self.tamanhoLado = tamanhoLado
        
        def mostrar_area (self):
            return self.tamanhoLado

        def mudar_valor_lado (self):
            return self.tamanhoLado**2
        
        
quadrado1=Quadrado(4)
print(f"A área do quadrado é {quadrado1.tamanhoLado}")
print("A area é:",quadrado1.mostrar_area())

quadrado2=Quadrado(6)
print(f"O valor mudado quadrado do quadrado é {quadrado2.tamanhoLado}")
print("A area modifcada é:",quadrado2.mudar_valor_lado())