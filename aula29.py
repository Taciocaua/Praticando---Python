"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input("Escreva o numero que vai ser dobrado: ")
print(numero_str.isdigit())

try:
    numero_str.isdigit()
    numero_float = float(numero_str)
    print("Float", numero_float)
    print(f"O do numero {numero_str} é {numero_float * 2}")
except:  
    print("Numero não foi digitado corretamente!")    