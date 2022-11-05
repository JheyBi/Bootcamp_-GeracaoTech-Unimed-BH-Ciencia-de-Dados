def somar(x,y):
    return x+y

def calcular_total(numeros):
    return sum(numeros)

def antecessor_sucessor(x):
    antecessor = x-1
    sucessor = x+1

    return antecessor, sucessor


print(somar(10,20))
print(antecessor_sucessor(5))
print(calcular_total([10, 20, 30]))