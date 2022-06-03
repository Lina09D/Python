'''3.	Elabore un programa POO, en el cual se declaren dos valores enteros 
por teclado utilizando el método __init__. Calcular con estos dos valores 
la suma, resta, multiplicación y división. Utilizar un método para cada una 
de las operaciones e imprimir los resultados obtenidos. 
Llamar a la clase Calculadora.'''
# declaramos la clase Calculadora
class Calculadora:
    # declaramos el metodo __init__
    def __init__(self):
        self.num1=int(input("Ingrese un número: "))
        self.num2=int(input("Ingrese otro número: "))
 
    # declaramos el metodo mostrar
    def mostrar(self):
        print("Número1: ",self.num1)
        print("Número2: ",self.num2)

         # declaramos el metodo resultado
    def resultado(self):
          print('El resultado de la suma es:', self.num1 + self.num2)
          print('El resultado de la resta es:', self.num1 - self.num2)
          print('El resultado de la multiplicación es:', self.num1 * self.num2)
          print('El resultado de la división es:', self.num1 / self.num2)
        
# bloque principal
num1=Calculadora()
num1.mostrar()
num1.resultado()