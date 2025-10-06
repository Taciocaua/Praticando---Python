"""
Operadores de atribuição
= += -= *= /= //= **= %=
""" 

contador = 0 

while contador <= 20:
    contador += 1

    if contador == 6:
        print("O '6' não vai aparecer!")
        continue

    if contador >= 10 and contador <= 15:
        print("Não vou mostrar", contador)
        continue

    print(contador)

    if  contador == 20:
        break

print("A contagem acabou") 