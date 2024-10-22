#04) Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa
#anual de crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de
# crescimento de 1,5% anual.

#Faça um programa que calcule e escreva o número de anos
# necessários para que a população do País A ultrapasse ou inguale 
#a população do país B, mantidas as taxas de cresciemnto.

a=80000
b=200000

cont=0

while a<= b:
    a=a+(a*3/100)
    b=b+(b*1.5/100)
    cont=cont+1
print(cont)

#05) Altera o programa anterior permitido ao usuário informar as 
# populações e as taxas de crescimento iniciais. Valide a entrada e 
#permite repetir a operação.
while True:
    x = int(input("1 - Informar dados\n 0 - Sair"))
    if x == 1:
        a=float(input("Digite a população do País A ="))
        b=float(input("Digite a população do País B ="))
        c=float(input("Digite a porcentagem do País A ="))
        d=float(input("Digite a porcentagem do País B ="))

        cont=0

        while a<= b:
            a=a+(a*c/100)
            b=b+(b*d/100)
            cont=cont+1  
    elif x == 0:
        break
    print(cont)

#06) O sr Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99
# e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa
# registradora rudimentar. O programa deverá receber um numero desconhecido de valores
#referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador 
#para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o 
#valor  em dinheiro que o cliente forneceu, para então calcular e mostar o valor do troco.
#Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.
#A saída deve ser conforme o exemplo abaixo:

# while True:
#      total=0  
#     a=int(input("Informar o valor do item: "))
#     total= total+a
#     print(total)
    
#     if total==0.0:
#        break
#     print(total)

#     while True:

#       x=float(input("Informe o valor do pagamento: "))
# if total>x:
#             print("O valor insuficiente ")
#      elif total <=x:
#      z=x-total
#      print("Seu troco foi de " , z)
#      break

#09) Em uma eleição presidencial existem quatro candidatos. 
#Os votos são informados através de códigos. Os dados utilizados 
# para a contagem dos votos obedecem á seguinte codificação:
#1,2,3,4 = Voto para os respectivos canditados:
#0= voto nulo (Qualquer outro número, menos o 0 e os canditados)
#6=voto em branco

#Elabore um programa que leia o código votado por vários eleitores.Como finalizar da entrada de dados,
#considere o código zero.
#Ao final, calcule e escreva:
#total de votos para cada candidato:
#total de votos nulos
#total de votos em brancos


