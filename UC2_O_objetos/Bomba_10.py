# 10 - Classe Bomba de Combustível: Faça um programa completo utilizando classes e
# métodos que:
# Possua uma classe chamada BombaCombustível, com no mínimo esses atributos:
# tipoCombustivel.
# valorLitro
# quantidadeCombustivel
# Possua no mínimo esses métodos
# abastecerPorValor( )- método onde é informado o valor a ser abastecido e
# mostra a quantidade de litros que foi colocada no veículo
# abastecerPorLitro( )- método onde é informado a quantidade em litros de
# combustivel e mostra o valor a ser pago pelo cliente
# alterarValor()- altera o valor do litro do combustivel.
# alterarCombustivel( ) - altera o tipo do combustível.
# alterarQuantidadeCombustivel( )- altera a quantidade de combustivel restante
# na bomba
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade
# de combustivel total na bomba

class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecerPorValor(self, valor):
       
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            print(f"Abastecido {litros_abastecidos:.2f} litros por R${valor:.2f}.")
            print(f"Quantidade de combustível restante: {self.quantidade_combustivel:.2f} litros.")
        else:
            print("Quantidade de combustível insuficiente na bomba.")

    def abastecerPorLitro(self, litros):

        if litros <= self.quantidade_combustivel:
            valor_a_pagar = litros * self.valor_litro
            self.quantidade_combustivel -= litros
            print(f"Valor a ser pago por {litros} litros: R${valor_a_pagar:.2f}.")
            print(f"Quantidade de combustível restante: {self.quantidade_combustivel:.2f} litros.")
        else:
            print("Quantidade de combustível insuficiente na bomba.")

    def alterarValor(self, novo_valor):
        self.valor_litro = novo_valor
        print(f"Novo valor do litro de combustível: R${self.valor_litro:.2f}.")

    def alterarCombustivel(self, novo_tipo):
        self.tipo_combustivel = novo_tipo
        print(f"Tipo de combustível alterado para: {self.tipo_combustivel}.")

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade
        print(f"Quantidade de combustível alterada para: {self.quantidade_combustivel:.2f} litros.")

bomba = BombaCombustivel("Gasolina", 5.50, 1000.0)

bomba.abastecerPorValor(50.00)  
bomba.abastecerPorLitro(5)  

bomba.alterarValor(6.00)  
bomba.alterarCombustivel("Álcool")  
bomba.alterarQuantid
