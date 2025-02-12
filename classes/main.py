
from Pessoa import Pessoa,PF,Pj

while True:
    tipo=int(input("Digite 1-para Pessoa fisica\n2-Pessoa Juridica"))

    if tipo==1:
     f=PF()
     f.PFisica()

    if tipo==2:
     f=Pj()
     f.Pjuridica()

