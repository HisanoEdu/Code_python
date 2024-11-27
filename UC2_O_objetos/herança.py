
#27/11/2024

#Vamos inplementar as classes Account e Business Account e fazer alguns testes. holder= titular  balance= equilibrio

class Account:
    def __init__(self,number: int, holder: str, balance: float ):
        self.number=number
        self.holder=holder
        self.balance=balance

def withdraw(self, amout: float):
    #implementar o saque
      if amout > 0:                                        # if amout >0 and amout>= self.balance:
            self.balance-= amout

def deposit(self,amout: float): 

     if amout> 0:
      self.balance+=amout


class BussinesAccount (Account):
    def __init__(self, number: int , holder: str , balance: float , loanLimit):
         super().__init__(number,holder,balance)
         self.loanLimit=loanLimit

         def loan(self,amout:float):
              if amout<=self.loan_limit:
                  self.balance+=amout
              else:
                  print("Emprestimo excede o limite permitido")
           
def __str__(self):
 return f"Bussines conta:({self.number}, {self.holder}, balance:{self.balance},{self.balance:2f},loanlimit:{self.loanlimit})"

acc= Account(123,"Jhonathan" , 3.50)
print(f"Primeiro print:{acc}")
acc.deposit(5.50)
print(f"Segundo print:{acc}")
acc.withraw(1.50)
print(f"Terceiro print: {acc}")

b_acc=BussinesAccount(321, "Padaria" , 500.0,2000.0)
print(f"1 BC: {b_acc}")
b_acc.loan(2000.0)
print(f" 2 BC:{b_acc}")


