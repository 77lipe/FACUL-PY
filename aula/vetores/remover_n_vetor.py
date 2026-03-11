v = [2,4,5,6,7,8,9]

print(v)
val = int(input("Qual valor deseja remover? "))

if val in vetor:
    vetor.remove(val)
    print("Vetor após remoção:", v)
else:
    print("Esse valor não está presento no vetor!!")


## pop() -> deleta valor de uma lista, pega por posição
## remove() -> remove um valor específico de uma lista