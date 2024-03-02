#--------Class,methods,atributes, objects--------------------------------
class Vehicle:
    #los atributos viven en la clase fuera de los metodos
    def __init__(self, make, model, color):
        """Este metodo sirve para inicializar el objeto que se crea, recuerden las classes son un molde, y las instancias son los objetos creados con esa clase"""
        self.make = make
        self.model = model
        self.color = color
        self.is_running = False
    
    def start_engine(self):
        """Este metodo sirve para encender el motor del vehiculo"""
        self.is_running = True
        print("El vehiculo a iniciado.")
    
    def stop_engine(self):
        """Este metodo sirve para apagar el motor del vehiculo"""
        self.is_running = False
        print("El vehiculo se a detenido.")
    
    def change_color(self, new_color):
        """Este metodo sirve cambiar el color del vehiculo"""
        self.color = new_color
        print(f"El nuevo color del  vehiculo es: {self.color}.")

    def print_atributs(self):
        print(self.color,self.make,self.model)

#en esta linea estamos creando un objeto, otra forma que vamos a encontrar para decir esto es que estamos instanciando una clase
vehicle1 = Vehicle("peugeot","301","Blanco")
print (vehicle1.make, vehicle1.color, vehicle1.model)
vehicle2 = Vehicle("Ford","Explorer","2002")
vehicle2.print_atributs()
print (vehicle2.make)
# Iniciamos el motor del vehiculo 1 
vehicle1.start_engine()
#cambiamos el color del vehiculo 1 
vehicle1.change_color("Red")
#--------en esta linea estamos creando la clase persona--------------------------------
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad

    def resumen(self):
        return f"Resumen, del estudiante: {self.get_nombre()} tiene {self.get_edad()} años."


class Estudiante(Persona):
    def __init__(self, nombre, edad, programa, cohorte):
        super().__init__(nombre, edad)
        self.programa = programa
        self.cohorte = cohorte

    def estudiar(self):
        return f"{self.get_nombre()} está estudiando {self.programa} en la cohorte {self.cohorte}."


# Obtener datos del usuario
print()
print("Hola estudiante de análisis de datos, espero te encuentres bien.")
print("Ingresa los siguientes datos")
print()
nombre = input("Escribe tu nombre completo: ")
edad = int(input("Escribe tu edad en números: "))
programa = input("Escribe el programa académico: ")
cohorte = int(input("Escribe tu cohorte en números: "))

# Crear un objeto de la clase Estudiante
estudiante1 = Estudiante(nombre, edad, programa, cohorte)

# Acceder a atributos y métodos de la clase Estudiante y de su clase base Persona
print()
print(estudiante1.resumen())
print("Nombre:", estudiante1.get_nombre())
print("Edad:", estudiante1.get_edad())
print("Programa:", estudiante1.programa)
print("Cohorte:", estudiante1.cohorte)
print(estudiante1.estudiar()) 
