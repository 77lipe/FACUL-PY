vetor = []

# -> Big-O (1)
for i in range(5):
    num = int(input("Digite um número desejado: "))
    vetor.append(num)

print("Vetor final:", vetor)

###

for n in range(len(vetor)): #   len -> Conta as posições dentro da lista -> se quiser pegar/saber qual o o valor e sua posição.
    print("Elemento:", n, ":", vetor[n])    # -> n pega as posições // vetor[n] pega o valor referente a posição

###

cont = 0
for j in vetor:
    cont+=j

print("Soma de todos os valores:", cont)

