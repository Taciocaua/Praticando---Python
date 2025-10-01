# Operadores in e not in 
# Strings são interáveis
#  0 1 2 3 4 
#  T Á C I O 
# -5-4-3-2-1 

nome = "Tácio"
print(nome[1])
print(nome[-4]) 
print(10*'=')
      
print('á' in nome) #True 
print('Tá' not in nome) #False  
print(10*'=') 

nome = input("Digite o seu nome: ")
encontrar = input("Digite o que deseja econtrar: ")

if encontrar in nome:
    print("Está no nome")
else:
    print("A escrita " f"{encontrar} não está no nome") 