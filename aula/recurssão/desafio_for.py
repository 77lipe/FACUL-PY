b = int(input("Digite o número base: "))
p = int(input("Digite o número de potência: "))

total = 1
for i in range(1, p+1):
    total *= b

print(total)