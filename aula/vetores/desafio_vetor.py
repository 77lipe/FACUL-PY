v = [2,5,8,12,15,20]

posicao=0
for i in range(5):
    val = int(input("Digite um valor: "))
    while posicao < len(v) and v[posicao] < val:
        posicao+=1
    v.insert(posicao, val)

print("Vetor final:", v)
