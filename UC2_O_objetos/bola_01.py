#25/11/2024

class Bola():
        def __init__(self, cor, circunferencia, material):
            self.cor= cor
            self.circunferencia=circunferencia
            self.material=material

troca_cor = Bola ('Azul','10x10', "Latex")
print(troca_cor.material)

mostra_cor = Bola ('Vermelho', '20x20', 'Couro')
print(mostra_cor.circunferencia)