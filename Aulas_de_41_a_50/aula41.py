""" Calculadora usando WHILE """

while True:
    numero1 = input("Digite um numero: ")
    numero2 = input("Digite outro numero: ")
    operador = input("Digite o operador (+,-,*,/): ")

    num1_float = 0
    num2_float = 0

    try:   
        num1_float = float(numero1)
        num2_float = float(numero2)
        numeros_validos = True
    except:  
        
        numeros_validos = None 
    
    if numeros_validos is None:
        print("Um dos numeros digitados são invalidos.")
        continue 
    print("Resultado abaixo ↓")
    
    if operador == '+':
        print(num1_float + num2_float)

    elif operador == '-':       
        print(num1_float - num2_float)

    elif operador == '*':   
        print(num1_float * num2_float)

    elif operador == '/':  
        print(num1_float / num2_float)

    else:
        print("Algo no codigo está errado!") 

    sair = input("Quer sair? [s]im: ").lower().starswitch()

    if sair is True:
        break   
    print("Você saiu da calculadora!")
