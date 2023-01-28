class padre():
    x=1

class operasbas(padre):
    #Definir propiedades de clase
    num1 = 0
    num2 = 0
    res = 0

    #Definir constructor de la clase
    
    #Definimos los métodos de la clase
    def suma(self, a, b):
        self.num1 = a
        self.num2 = b
        return "La suma de " + a + " + " + b + " es =" + a+b 
    

