
# 08)Classe Macaco: Desenvolva uma classe Macaco, que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(),
# verBucho() e digerir(). 
# Faça um programa ou teste interativamente, 
# criando pelo menos dois macacos, alimentando-os 
# com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. 
# Experimente fazer com que um macaco coma o outro. 
# É possível criar um macaco canibal?

class Macaco:
    def _init_(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):

        self.bucho.append(alimento)
        print(f"{self.nome} comeu {alimento}.")

    def verBucho(self):
        if self.bucho:
            print(f"O bucho de {self.nome} contém: {', '.join(map(str, self.bucho))}.")
        else:
            print(f"O bucho de {self.nome} está vazio.")

    def digerir(self):
        if self.bucho:
            print(f"{self.nome} digeriu: {', '.join(map(str, self.bucho))}.")
            self.bucho = []
        else:
            print(f"Nada para digerir no bucho de {self.nome}.")

macaco1 = Macaco("Macaco1")
macaco2 = Macaco("Macaco2")

macaco1.comer("Banana")
macaco1.verBucho()
macaco1.comer("Maçã")
macaco1.verBucho()
macaco1.comer("Laranja")
macaco1.verBucho()

macaco2.comer("Uva")
macaco2.verBucho()
macaco2.comer("Pêra")
macaco2.verBucho()
macaco2.comer("Melancia")
macaco2.verBucho()

macaco1.comer(macaco2)
macaco1.verBucho()

macaco1.digerir()
macaco1.verBucho()

macaco2.digerir()
macaco2.verBucho()