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