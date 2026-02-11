valor1 = int(input("Digite o primeiro valor:\n"))
valor2 = int(input("Digite o segundo valor:\n"))
valor3 = int(input("Digite o terceiro valor:\n"))


def sum():
    soma1 = valor1 + valor2
    soma2 = valor1 + valor3
    soma3 = valor2 + valor3

    over = [soma1, soma2, soma3]

    return over

print(sum())

if sum()[0] > valor3:
    print(f'A soma de {valor1} com {valor2} FORMAM um Triângulo!!')
elif sum()[1] > valor2:
    print(f'A soma de {valor1} com {valor3} FORMAM um Triângulo!!')
elif sum()[2] > valor1:
    print(f'A soma de {valor2} com {valor3} FORMAM um Triângulo!!')
else:
    print(f'Não é possível formar um triângulo')




