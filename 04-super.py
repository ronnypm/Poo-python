class Persona():
    
    def __init__(self,nombre,edad,lugar_residencia):
        self.nombre = nombre
        self.edad = edad 
        self.lugar_residencia = lugar_residencia


    def descripcion(self):
        print(f'nombre:{self.nombre}\nEdad:{self.edad}\nDireccion:{self.lugar_residencia}')




class Empleado(Persona):
    def __init__(self,salario, antiguedad,nombre_empleado,edad_empleado,residencia_empleado):
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad


    def descripcion(self):
        super().descripcion()
        
        print(f'Salario:{self.salario}\nAntiguedad:{self.antiguedad}')


Ronny = Empleado(1000,14,'Ronny',25,"Peru")
Ronny.descripcion()

print(isinstance(Ronny,Persona))





# -------------------------------------------

from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def calcular_salario(self):
        pass  # Los hijos deben sí o sí implementar este método

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"



class Programador(Empleado):
    def __init__(self, nombre, edad, lenguaje):
        super().__init__(nombre, edad)  # Atributos de la clase padre
        self.lenguaje = lenguaje        # Atributo propio

    def calcular_salario(self):
        return 4000  # Un salario fijo por ejemplo

    def __str__(self):
        return f"{super().__str__()} - Programador en {self.lenguaje}"


class Diseñador(Empleado):
    def __init__(self, nombre, edad, herramientas):
        super().__init__(nombre, edad)
        self.herramientas = herramientas

    def calcular_salario(self):
        return 3500

    def __str__(self):
        return f"{super().__str__()} - Diseñador usando {', '.join(self.herramientas)}"

empleados = [
    Programador("Ana", 28, "Python"),
    Diseñador("Luis", 30, ["Photoshop", "Figma"])
]

for empleado in empleados:
    print(empleado)
    print(f"Salario: ${empleado.calcular_salario()}")
    print("------")
