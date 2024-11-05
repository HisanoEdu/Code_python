#dicionário em python

# tradutor={}
# tradutor["pineapple"] ="abacaxi"
# tradutor["apple"]="maça"
# tradutor["orange"] ="Laranja"
# print(type(tradutor))
# print(tradutor)

# tradutor1={}
# tradutor1={"pineapple":"abacaxi", "apple": "maça","orange":"laranja"}
# print(type(tradutor1))
# print(tradutor1)


# # o exemplo mostra como usar uma chave para pesquisar o valor correspondente

# tradutor1={}
# tradutor1={"pineapple":"abacaxi", "apple": "maça","orange":"laranja"}
# print(tradutor1["apple"])

# tradutor1={}
# tradutor1={"pineapple":"abacaxi", "apple": "maça","orange":"laranja"}
# print(tradutor1)
# del(tradutor1["apple"])
# print(tradutor1)

#del serve para remover um par chave-valor de um dicionário.

# tradutor1={}
# tradutor1={"pineapple":"abacaxi", "apple": "maça","orange":"laranja"}
# print(tradutor1)
# print(tradutor1.pop('banana','fruta não encontrada'))
# print(tradutor1)

#clear limpa o dicionário, remove todos os elementos
#.tradutor1.clear()

# tradutor1.clear()

# tradutor1={}
# tradutor1={"pineapple":"abacaxi", "apple": "maça","orange":"laranja"}
# print("pineapple" in tradutor1)


# tradutor1={}
# tradutor1={"pineapple":"abacaxi", "apple": "maça","orange":"laranja"}
# print("banana" in tradutor1)

#o comando in verifica apenas as chaves do dicionário, não os valores.
#Para obtermos valores, podemos usar o método values():

# print('laranja'in a.values())
# a=tradutor

# tradutor1={}
# tradutor1={"pineapple":"abacaxi", "apple": "maça","orange":"laranja"}
# print(tradutor1)
# tradutor1["apple"]="goiba"
# print(tradutor1)


#É possivel criar um dicionário dentro uma chave de um dicionário

# dados={
#     'Crossfox': {'km': 35000,'ano':2005},
#      'DS5':{'km':17000,'ano':2015},
#      'fusca':{'km':13000,'ano':1979},
#      'jetta':{'km':56000,'ano':2011},
#       'Passat':{'km':62000,'ano':1999}
#       }
# print(dados)

# #get retorna ao valor a uma chave especifica

# dados={
#     'Crossfox': {'km': 35000,'ano':2005},
#      'DS5':{'km':17000,'ano':2015},
#      'fusca':{'km':13000,'ano':1979},
#      'jetta':{'km':56000,'ano':2011},
#       'Passat':{'km':62000,'ano':1999}
#       }

# print(dados.get('Gol','veículo não encontrado'))

#Tratamneto de exceção

#try,except,else e finally

#Try testa o bloco de código

#try
# a=int(input("digite uma palavra "))

# #except:

# print("Digite apenas números ")

# #O bloco try conterá erro caso seja 
# #digitada uma letra, e o excepet trará 
# #uma ação caso ocorra erro.

# print("Erro desconhecido ")

#finally 

#O finally executa independete de erros:
#try

# a=int(input("Digite uma palavra = "))
# #except ValueError:
# print("Digite apenas números ")
# #except
# print("Erro desconhecido ")
# #finally
# print("Final do algoritmo ")

#Tratamento de erros

# 4+spam*3
# NameError

# while True print('Hello world')
# SyntaxError




#calculadora 
#Elabore uma calculadora com todas as operações basicas, utilize try e except

# while True:

#     opcao=int(input("Escolha a operação desejada \n1.Multiplicação \n2.Divisão \n3.Adição \n4.Subtração \n5.Sair"))
#     print(opcao)
#     if opcao==1:
#         valor1=int(input("Digite um valor "))
#         valor2=int(input("Digite um valor "))
#         a=valor1**valor2
#         print("Multiplicação" , a)


#     if opcao==2:
#         valor1=int(input("Digite um valor "))
#         valor2=int(input("Digite um valor "))
#         b=valor1/valor2
#         print("Divisão" , b)

#     if opcao==3:
#         valor1=int(input("Digite um valor "))
#         valor2=int(input("Digite um valor "))
#         c=valor1+valor2
#         print("Adição" ,c)

#     if opcao==4:
#        valor1=int(input("Digite um valor "))
#        valor2=int(input("Digite um valor "))
#        d=valor1-valor2
#        print("Subtração",d)

#     if opcao==5:
#         print("Sair")
#         break
#     else:
#         print("Opção invalida")
    
#     print ("\n\n")





 #except ValueError:

while True:
 try:
        opcao=int(input("Escolha a operação desejada \n1.Multiplicação \n2.Divisão \n3.Adição \n4.Subtração \n5.Sair"))
        if opcao==1:
            n1=float(input("Digite um valor "))
            n2=float(input("Digite um valor "))
            n3=float(input("Digite um valor "))

            n3=n1*n2
            print(n3)

        elif opcao==2:
            n1=float(input("Digite um valor "))
            n2=float(input("Digite um valor "))
            n3=float(input("Digite um valor "))

            n3=n1/n2
            print(n3)

        elif opcao==3:
            n1=float(input("Digite um valor "))
            n2=float(input("Digite um valor "))
            n3=float(input("Digite um valor "))

            n3=n1+n2
            print(n3)

        elif opcao==4:
            n1=float(input("Digite um valor "))
            n2=float(input("Digite um valor "))
            n3=float(input("Digite um valor "))

            n3=n1-n2
            print(n3)

        else:
            print("Opção inválida")

 except ValueError:
    print("Digite apenas números")   
 except:
  print("Erro desconhecido")


