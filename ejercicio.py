
numero = int(input("Numero: "))

def funcion(x):
    for i in range(1,11):
        print("{} x {} = {}".format(x, i, x*i))

funcion(numero)