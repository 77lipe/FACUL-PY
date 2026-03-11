
v = [3,7,10,15]
n = int(input("Digite um número: "))

for i in range(len(v)):
    if v[i] == n:
        print("Esse número está presento no vetor!!\nValor encontrado na posição:", i)
        break
    else:
        print("Este valor não está presente no vetor!!")
        break



#  OUTRA FORMA

encontrou = False
for i in range(len(v)):
    if v[i] == n:
        print("Esse número está presento no vetor!!\nValor encontrado na posição:", i)
        encontrou = True
        break

if encontrou == False:
    print("Esse número não foi encontrado no vetor!!")