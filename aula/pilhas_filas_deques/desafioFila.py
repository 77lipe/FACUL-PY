

capacidade = 5
fila = []

def enfileirar(valor):
    fila.append(valor)
    return fila

def desenfileirar():
    fila.pop(0)
    return fila


while True:
    escolha = int(input("Digite sua escolha: \n1 - Enfileirar\n2 - Desenfileirar\n3 - Sair\n"))

    if escolha == 1:
        for i in range(capacidade):
            valor = int(input("Qual valor deseja colocar: "))
            if len(fila) < capacidade:
                print("Fila:", enfileirar(valor))
            else:
                print("Fila Cheia!")
    elif escolha == 2:
        if len(fila) > 0:
            print("Desempilhado:", fila[0], "\nPilha final:", desenfileirar())
        else:
            print("Fila Vazia!!")
    elif escolha == 3:
        break
    else:
        print("Opção inválida!!")
        break





