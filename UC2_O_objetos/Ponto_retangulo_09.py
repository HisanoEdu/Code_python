
# 09 - Classe Ponto e Retangulo: Faça um programa completo utilizando funções
# e classes que:
# Possua uma classe chamada Ponto, com os atributos x e y.
# Possua uma classe chamada Retangulo, com os atributos largura e altura.
# Possua uma função para imprimir OS valores da classe Ponto
# Possua uma função para encontrar o centro de um Retângulo.
# Você deve criar alguns objetos da classe Retangulo.
# Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior
# esquerdo do retângulo, que deve ser um objeto da classe Ponto
# A função para encontrar o centro do retângulo deve retornar o valor para um
# objeto do tipo ponto que indique os valores de x e y para o centro do
# objeto
# O
# valor do centro do objeto deve ser mostrado na tela
# Crie um menu para alterar os valores do retângulo imprimir o centro deste
# retângulo.

class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f'Ponto: ({self.x}, {self.y})')

class Retangulo:
    def __init__(self, ponto_inferior_esquerdo, largura=0, altura=0):
        self.ponto_inferior_esquerdo = ponto_inferior_esquerdo
        self.largura = largura
        self.altura = altura

    def centro(self):
        centro_x = self.ponto_inferior_esquerdo.x + (self.largura / 2)
        centro_y = self.ponto_inferior_esquerdo.y + (self.altura / 2)
        return Ponto(centro_x, centro_y)

    def alterar_valores(self, largura, altura):
        self.largura = largura
        self.altura = altura

def menu():
    ponto_inferior_esquerdo = Ponto(0, 0)

    retangulo = Retangulo(ponto_inferior_esquerdo, 5, 4)

    while True:
        print("\nMenu:")
        print("1. Imprimir centro do retângulo")
        print("2. Alterar dimensões do retângulo")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            centro = retangulo.centro()
            centro.imprimir()

        elif opcao == "2":
            nova_largura = float(input("Informe a nova largura: "))
            nova_altura = float(input("Informe a nova altura: "))
            retangulo.alterar_valores(nova_largura, nova_altura)
            print("Valores alterados com sucesso!")

        elif opcao == "3":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida! Tente novamente.")

menu()
