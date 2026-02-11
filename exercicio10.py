print("Tabuada")
number1 = int(input("Digite um número:\n"))

contador = 1
while contador < 11:
    result = number1 * contador
    print(f'{number1} x {contador} = {result}')
    contador += 1