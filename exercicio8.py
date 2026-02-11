number1 = float(input("Digite o primeiro valor:\n"))
number2 = float(input("Digite o segundo valor:\n"))

if number1 > number2:
    print(f'{number1} é Maior que {number2}')
elif number1 < number2:
    print(f'{number2} é Maior que {number1}')
else:
    print(f'{number1} e {number2} são IGUAIS!!')