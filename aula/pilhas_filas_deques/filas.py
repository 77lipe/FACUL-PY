
fila = []

fila.append(10)
fila.append(20)
fila.append(30)

print(fila)


# desenfileirar

if len(fila) > 0:
    removido = fila.pop(0)
    print("Removido", removido)
else:
    print("Fila vazia")
    
print("Fila final:", fila)