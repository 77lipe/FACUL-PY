v = [5,2,3,5,9,9,5]
val = int(input("Digite um valor: "))
cont = 0

for i in range(len(v)):
    if v[i] == val:
        cont+=1

print(f"O valor {val} está presente no vetor: {cont} vezes")