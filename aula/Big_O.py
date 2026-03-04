# Notação Big-O

# Tempo de execução para um algoritmo ser rodado / analisando a Complexidade de um algoritmo - chamado de notação Big-O

# - Como comparar algoritmos?
# - Considera difenças entre poder de processamento, sistema opcional, linguagem de programação
# - O quanto a complexidade do algoritmo aumenta de acordo com as entradas


# timeit -> devolve dados que representa a velocidade de processamento de um algoritmo / código


# Função Big-O(n)

def soma1(n):
    soma=0
    for i in range(n+1):
        soma +=i
    return soma

#print(soma1(10))
##%timeit soma1(10)

def soma2(n):
    return(n*(n+1) / 2)

#print(soma2(10))

def lista1():
    list = []
    for i in range(1000):
        list += [i]
    return list

#print(lista1())

def lista2():
    return range(1000)

#print(lista2())



## FUNÇÕES Big-O:

#   1 Constante
#   log(n) - Logaritmic
#   n linear
#   n log(n) - log linear
#   n^2 quadratic
#   n^3 cubic
#   2^n exponential

from math import log
import numpy as np
import matplotlib.pyplot as plt

b = np.linspace(1,10,100)
n.shape
np.ones(n.shape)


labels = ['Constant', 'Logarithimc', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponent']
big_o = [np.ones(n.shape), np.log(n), n, n* np.log(n), n**2, n**3, 2**n]

###

# O Big-O será operado apenas 1 vez, segundo a função (CONSTANTE):
lista = [1,2,3,4,5,6,7]
def constante(n):
    print(n[0])

print(constante(lista))

###

# O Big-O vai variar de acordo com a entrada da função (LINEAR):
def linear(n):
    for i in n:
        print(n)

###

# O Big-O é determinado pela quantidade de FORs (QUADRATIC)
def quadratic(n):
    for i in n:
        for j in n:
            print(i,j)
        print("---")



