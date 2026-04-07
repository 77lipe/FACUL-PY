
def potencia(b,p):
    if p == 1 or p == 0:
        return b
    return b * potencia(b, p-1)

print(potencia(3,3))