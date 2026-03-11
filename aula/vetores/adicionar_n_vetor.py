val = int(input("Digite um valor: "))

posicao = 0 

while posicao < len(v) and v[posicao] < val:
    posicao+=1

v.insert(posicao, val)

print("Vetor final:", v)