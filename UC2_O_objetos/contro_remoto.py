
class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura, quarto, marca):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
        self.quarto = quarto
        self.marca = marca

controle_remoto1 = ControleRemoto("Azul", 10, 5, 2,'Quarto', 'Hocku')
controle_remoto2 = ControleRemoto('Vermelho', 10, 5, 2, 'Cozinha', 'TCL')
controle_remoto3 = ControleRemoto('Verde', 10, 5, 2, 'Sala', 'Samsung')
controle_remoto4 = ControleRemoto('Preto', 10, 5, 2, 'Som', 'LG')
controle_remoto5 = ControleRemoto('Branco', 10, 5, 2, 'Portão', 'Philips')

def controle_quarto(botao):
    if botao == "NetFlix":
        print("abrir NetFlix")
    elif botao == "Power":
        print("desligar TV")
    else:
        print("Valor Inválido")

def controle_cozinha(botao):
        if botao == "CH":
            print("mudar canal")
        elif botao == "Mute":
            print("som desligado")
        else:
            print("Valor Inválido")

def controle_portao(self, botao):
        if botao == "5":
            print("Abrir Portão")
        elif botao == "1":
            print("Fechar")
        else:
            print("Valor Inválido")

def controle_som(self, botao):
        if botao == "+":
            print("aumentar volume")
        elif botao == "-":
            print("diminuir volume")
        else:
            print("Valor Inválido")

def controle_sala(self, botao):
        if botao == "A":
            print("Abrir cortina")
        elif botao == "F":
            print("Fechar cortina")
        else:
            print("Valor Inválido")

print(f"O controle remoto do {controle_remoto1.marca} é de cor {controle_remoto1.cor}.")
controle_quarto("Power")
print(f"O controle remoto da {controle_remoto2.marca} é de cor {controle_remoto2.cor}.")
controle_cozinha("Mute")
print(f"O controle remoto do {controle_remoto3.marca} é de cor {controle_remoto3.cor}.")
controle_sala("A")
print(f"O controle remoto da {controle_remoto4.marca} é de cor {controle_remoto4.cor}.")
controle_som("+")
print(f"O controle remoto do {controle_remoto5.marca} é de cor {controle_remoto5.cor}.")
controle_portao("1")