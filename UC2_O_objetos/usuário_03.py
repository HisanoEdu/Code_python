
class Usuario():
    def __init__(self, nome, email, cpf, plano, cartaoCredito, fone):
        self.nome=nome
        self.email=email
        self.cpf=cpf
        self.plano=plano
        self.cartaoCredito=cartaoCredito
        self.fone=fone

usuario1 = Usuario('Eduarda','eduarda@email.com',969755901, 'Premiun', 128 ,99004747)
print(f"O plano da{usuario1.nome} é o {usuario1.plano}")


usuario2 = Usuario('Raquel','raquel@email.com',95930143,'Padrão',128,9900099)
print(f"O plano da{usuario2.nome} é o {usuario2.plano}")


usuario3 = Usuario('Jamily','jamily@email.com',93225544,'Básico',128,9696969)
print(f"O plano da{usuario3.nome} é o {usuario3.plano}")
