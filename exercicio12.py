number1 = int(input("Digite um número:\n"))

for i in range(2,number1):
    primo = 0
    cont = number1 % i
    #print(f'Cont = {cont}, O valor de I: {i}')
    if cont == 0:
        primo = cont
        if primo == 0:
            print(f'O numero {number1} NÃO é um primo')
        else:
            print(f'{number1} é um número PRIMO')
        
        break   
        

