# função len #A função len() é empregada para obter o comprimento de uma sequencia qualquer em python
a="Eduarda"
print(len(a))

#função capitalize
a="eduarda"
print(a.capitalize())

#função upper
a="eduarda"
print(a.upper())

# função casefold
a="EDUARDA"
print(a.casefold())

#print("eduarda".upper())

#Como transformar todo o texto em minusculo.
#Função lower
a="EDUARDA"
print(a.lower())

#Identificar se todo o texto está em minusculo.

#Função islower
a="EDUARDA"
print(a.islower())
#false

#Identificar se todo o texto está em maiúsculo
#Função isupper

a="EDUARDA"
print(a.isupper())
#True

#Como verificar se uma string só possui números inteiros.

#função isdigit

a='12345'
print(a.isdigit())
#True

#O método replace serve para trocar todas as ocorrências de uma substring por outra em uma string.

#Função replace

a="Eduarda Naomi"
print(a.replace("Eduarda" , "Naomi"))

#O método split(sep) separa uma string usando sep como separador.
#retorna uma lista das substring 
#seu passado sem parâmetros substitui espaço por",".
#Ou substitui espaço por ","
#ou substitui ou parâmetro

a="Eduarda-Naomi-Hisano"
print(a.split("-"))

#O método find retorna onde a substring começa na string ("Primeira")
a="Eduarda Naomi Hisano"
print(a.find("Hisano"))

#Procurar uma palavra no documento, ele vai contar as os elementos que tiver tanto letra e número, para contar ele inicia com zero depois um, dois...

#O operador in verifica se uma substring é parte de uma outra string.

a="Eduarda Naomi Hisano"
print("Hisano" in a)

#O operador count retorna a frequência de ocorrencia do parâmetro passado.

a="Eduarda Naomi Hisano"
print(a.count("o"))

s="Olá, mundo!"
print(s[0])
print(s[2])
print(s[6])

# SUBSTRINGS A primeira posição da letra colocar o número por exemplo "A" vai ser "0"

s="Olá, mundo!"
print(s[-11])
print(s[-9])
print(s[-5])

#O= -11 L=-10 Á=-9  ,=-8  ESPAÇO-7 M=-6 U=-5 N=-4 D=-2 O=-2 !=-1 (No negativo é -1 e positivo é 0)

S="Olá, mundo!"
print(s[1:3])

#Se omitirmos o índice de inicio da fatia ou o de final(ou ambos), o ínicio e o final da string serão considerados, respectivamente.

s="Olá,mundo"
print(s[:3])


#EX 01

#Escrever um programa na linguagem python que conte o número de palavra em um texto, como entrada, um texto será digitado de forma interativa no teclado. Como saída será impreso o texto,bem como a quantidade de caracteres desse texto.

#texto=input("Escreva um texto")
#print(len(texto))

#EX 02 String
# Tamanho de string.Faça um programa que leia 2 string e 
#informe o conteúdo delas seguindo do seu comprimento.

#txt=input("Digite o seu nome")
#texto=input("Digite uma palavra")
#print(len(txt))
#print(len(texto))

#EX 03 
#Faça um programa que leia um nome e imprima as 4 primeiras letras do nome.

Nome=input("Digite o seu nome")
print(Nome.capitalize())

# 04 string
#Faça um programa que leia um nome e imprima apenas a letra do primeiro nome em maiúsculo.













