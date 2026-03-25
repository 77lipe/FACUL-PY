capacidade = 5

pilha = []




for i in range(capacidade):
    num = int(input("Digite o valor para empilhar na fila: "))
    if len(pilha) < capacidade:
        pilha.append(num)
        print("Item adicionado a pilha:", pilha)
    else:
        print("Pilha cheia")
        break
    
print("Pilha final:", pilha)