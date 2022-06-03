'''2.	Realizar un programa POO que conste de una clase llamada Alumno que 
tenga como atributos el nombre y la nota del alumno. Ingresar por teclado. 
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un
mensaje con el resultado de la calificación y si ha aprobado o no. 
Nota >=3 aprobó
'''
# declaramos la clase Alumno.
class Alumno:
    # declaramos el metodo __init__
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.nota=float(input("Ingrese su nota: "))
 
 
    # declaramos el metodo mostrar
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("nota: ",self.nota)

         # declaramos el metodo aprobo.
    # comprobara si el alumno aprobo o no.
    def aprobo(self):
        if self.nota >= 3:
          print("¡Felicidades! vas aprobando.", self.nota)
        else:
            print("¡Ojo! vas mal, ponte las pilas.", self.nota)
 
# bloque principal
persona1=Alumno()
persona1.mostrar()
persona1.aprobo()