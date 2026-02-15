number1 = int(input("Digite um número:\n"))        
        
for i in range(2, number1):
    primo = number1 % i 
    ultimo = i

    if primo == 0:
        print("Esse número NÃO é PRIMO!!")
        break

if primo != 0:
    print("Esse número é PRIMO!!")     
