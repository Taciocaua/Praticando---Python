"""
Iterando strings com while
"""     
nome = 'Tacio'

indice = 0 
novo_nome = " "
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f"*{nome}"
    indice += 1
  
print(novo_nome)    