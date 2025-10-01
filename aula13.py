"f-strings"
nome = 'Tácio' 
peso = 65.50 
altura = 1.75
imc = peso/(altura*altura)

linha_1 = f'{nome} tem {altura:.2f} de altura e pesa {peso}'
linha_2 = f'e o seu imc é {imc:.2f}' 

print(linha_1)
print(linha_2)

#Tácio pesa 65,50 
#A sua altura é 1.75
#O seu IMC é 21.3
