class operacionesBasicas():
    
    def suma(self, x,y):
        print("La suma de {} + {} = {}".format(x,y, x+y))

    def resta(self, x,y):
        print("La resta de {} - {} = {}".format(x,y, x-y))

    def multiplicacion(self,x,y):
        print("La multiplicacion de {} * {} = {}".format(x,y, x*y))

    def division(self, x,y):
        print("La division de {} / {} = {}".format(x,y, x/y))


def main():
    
    print("1 = Suma")
    print("2 = Resta")
    print("3 = Multiplicacion")
    print("4 = Division")
    print("5 = Salir")

    opcion = int(input("Ingresa la opcion: "))

    numero1 = int(input("Ingresa el numero 1: "))
    numero2 = int(input("Ingresa el numero 2: "))

    obj = operacionesBasicas()

    while opcion != 5:

        if opcion == 1:
            obj.suma(numero1, numero2)
        elif opcion == 2:
            obj.resta(numero1, numero2)
        elif opcion == 3:
            obj.multiplicacion(numero1, numero2)
        elif opcion == 4:
            obj.division(numero1, numero2)
        else:
            print("Opcion erronea")

        print("1 = Suma")
        print("2 = Resta")
        print("3 = Multiplicacion")
        print("4 = Division")
        print("5 = Salir")

        opcion = int(input("Ingresa la opcion: "))

    print("Adios!!")

if __name__ == "__main__":
    main()
