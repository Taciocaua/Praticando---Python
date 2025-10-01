"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input("Digite um numero= ")

try:
    numero = int(entrada)

    if numero % 2 == 0:
        print("O numero é par")
    else:
        print("O numero é ímpar")
except:
    print("Isso não é numero")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = int(input("Qual é o horario atual?"))

if  0 <= hora <=11:
    print("Bom dia!")

elif 12<= hora <=17:
    print("Boa tarde")

elif 18<= hora <=23:
    print("Boa noite")

else:
    print("Horario errado, digite entre 0 a 23 ")        

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Qual o seu primeiro nome? ")
tamanho = len(nome)

if tamanho <=4:
    print("Seu nome é curto!")

elif tamanho ==5:
    print("Seu nome é normal!")

elif tamanho >=6:
    print("Seu nome é muito grande")
