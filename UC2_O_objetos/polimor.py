#polimorfismo 28/11/24 polimorfismo é a classe filho

class super:
    def hello(self):
        print("Olá,sou a superclasse")

teste=super()
teste.hello()

# Agora o resultado
# Olá, sou a superclasse

class super:
    def hello(self):
        print("Olá, sou a superclasse!")

class Sub(super):
    def hello(self):
        print("Olá, agora sou a subclasse agora!")
teste=Sub()
teste.hello()

class Subsub(Sub):
    def hello(self):
        print("Olá, sou a Subsubclasse agora")
teste=super()
teste.hello()


class Subsub(Sub):
    def hello(self):
        print("Olá, sou a Subsubclasse agora")
teste=Subsub()
teste.hello()


