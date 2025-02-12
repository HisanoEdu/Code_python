
import math

x=3.5
print(math.ceil(x))


math.fabs(x)
#retorna o valor absoluto de x


import math
x=-3
print(math.fabs(x))

import math


# math.factorial(n)

x=3
print(math.factorial(x))

#obs:Mudar as variaveis para não deixar tudo igual

# math.floor(x)

import math

z=3.5
print(math.floor(x))

# math.isqrt(n)

# Retrona a raiz quadrada inteira do inteiro negativo n.

#SORT retorna float

import math

X=81
print(math.isqrt(x))

#math.pow(x,y)
#retorna x elevado a potencia de y

import math

x=2
y=10
print(math.pow(x,y))

#Datime
#fornece classes para maipulação de datas e horas

import datetime
print(datetime.date.today())

#Metodo strflitime()
#Altera a data e ano na string

import datetime

print(datetime.date.today().strftime('%d/%m/%y'))


#Umas das vanatgens da classe datetime é 
#que ela consegue cuidar da data e do horario ao mesmo tempo.

import datetime
print(datetime.datetime.now())

#foramatando datas em strings usando o metodo striflitime()

import datetime
print(datetime.datetime.no().strflime("%d/%m/%y/%h/%m"))


import time

a=0
x=time.perf_counter()
while a<10000:
    print(a)
    a+1
    y=time.perf_counter()
    print(y-x)


#Em dupla pesquise duas biblioteca do python, explique o funcionamneto dela,
#com algumas f
