number1 = float(input("Digite o Primeiro número:\n"))
number2 = float(input("Digite o Segundo número:\n"))
number3 = float(input("Digite o Terceiro número:\n"))

def numeroMaior(): 
    if number1 > number2 and number1 > number3:
        print(f'O Número maior é {number1}!!')
    elif number2 > number1 and number2 > number3:
        print(f'O Número maior é {number2}!!')
    elif number3 > number1 and number3 > number2:
        print(f'O Número maior é {number3}!!')
    elif number1 == number2 and number1 == number3:
        print(f'Todos os números são iguais!!')

def numeroMenor():
    if  number1 < number2 and number1 < number3:
        print(f'O Número menor é {number1}!!')
    elif number2 < number1 and number2 < number3:
        print(f'O Número menor é {number2}!!')
    elif number3 < number1 and number3 < number2:
        print(f'O Número menor é {number3}!!')
    elif number1 == number2 and number1 == number3:
        print(f'Os Números sõa iguais!!') 


#print(numeroMaior())
numeroMaior()
numeroMenor()