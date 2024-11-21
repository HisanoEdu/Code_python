#Numpy

import numpy as np
array_3d=np.array([[[1,2,3],[4,5,6],[7,8,9]],
[[10,11,12],[13,14,15],[16,17,18]],[[19,20,
21],[22,23,24],[25,26,27]]])

print(array_3d)

x=np.random.rand(1)
print(x)

n=np.arange(2,11,2)
print(n)


#ex01

import numpy as up

y=np.random.rand(2,5)
print(y)
print(np.sum(y))
print(np.min(y))
print(np.max(y))
print(np.mean(y))

#ex02

numb=np.random.rand(0,20)
print(numb)

#PyDantic

from pydantic import BaseModel
class Usuario(BaseModel):
    nome:str
    idade:int
    email:str
usuario=Usuario(nome="João",idade=54,email="joao@exemplo.com")

print(usuario.nome)
print(usuario.idade)
print(usuario.email)


#Exercio 01: crie um modelo que contenha: Nome,idade,sexo 
from pydantic import BaseModel
class Usuario(BaseModel):
    nome:str
    idade:int
    sexo=str
usuario=Usuario(nome="Duncan Vizla",idade=50,sexo="Masculino")

print(usuario.nome)
print(usuario.idade)
print(usuario.sexo)



