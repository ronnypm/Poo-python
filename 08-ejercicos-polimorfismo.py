# class Perro():
#     def hacer_sonido(self):
#         print('Gua Gua!')

# class Gato():
#     def hacer_sonido(self):
#         print('Mia Miauuu!')

# #usuamos polomorfismo aqui

# animales = [Perro(),Gato()]

# for animal in animales:
#     animal.hacer_sonido()#llama al metodo segun su clase


# class Persona():
#     def __init__(self,nombre,edad):
#         self.nombre = nombre
#         self.edad = edad 


#     def  description(self):
        
#         print( f'Nombre:{self.nombre}\nEdad:{self.edad}')
    
# class Empleado(Persona):
#     def __init__(self, nombre, edad, salario):
#         super().__init__(nombre, edad)

#         self.salario = salario


#     def description(self):
#         super().description()

#         print( f'Salario:{self.salario}')



# persona1 = Persona('Juan',30)
# empleado1 = Empleado('Ronny',26,2500)
        
# persona1.description()
# empleado1.description()


# class Persona():
#     def __init__(self, nombre, edad):
#         self.nombre = nombre 
#         self.edad = edad

#     def description(self):

#         return f'nombre:{self.nombre}\nEdad:{self.edad}'

# class Estudiante(Persona):
#     def __init__(self, nombre, edad, carrera):
#         super().__init__(nombre, edad)

#         self.carrera = carrera


#     def description(self):
#         super().description() 

#         return f'nombre:{self.nombre}\nEdad:{self.edad}\nCarrera:{self.carrera}'
    

# class Profesor(Persona):
#     def __init__(self, nombre, edad, materia):
#         super().__init__(nombre, edad)

#         self.materia = materia

#     def description(self):
#         super().description()
#         print('\nProfesor')
#         return f'nombre:{self.nombre}\nEdad:{self.edad}\nMateria:{self.materia}'
    
# #Lista de personas con distinto tipos
# Personas = [Estudiante('Juan',20,'Redes y telecomunicaciones'),Profesor('Lavalle',35,'Redes convergentes')]


# #Aplicamos polimorfismo
# for persona in Personas:
#     print(persona.description())

# # Aquí el método descripcion() tiene un comportamiento distinto en cada subclase. Eso es polimorfismo.

# print(id(persona))
# print(id(persona))


# class Persona():
#     def __init__(self, nombre, edad):
#         """esto pasa"""

#         self.nombre = nombre 
#         self.edad = edad
        

#     def description(self):

#         return f'Nombre:{self.nombre}\nEdad:{self.edad}'
    
# class Alumno(Persona):
#     def __init__(self, nombre, edad, notas):
#         super().__init__(nombre, edad)

#         self.notas = notas

#     def description(self):
#         super().description()
#         print('\nAlumno')
#         return f'Nombre:{self.nombre}\nEdad:{self.edad}\nNotas:{self.notas}'
     

# class Profesor(Persona):
#     def __init__(self, nombre, edad, curso):
#         super().__init__(nombre, edad)

#         self.curso = curso
    
#     def description(self):
#         super().description()
#         print('\nProfesor')
#         return f'Nombre:{self.nombre}\nEdad:{self.edad}\nCursos:{self.curso}'
    
# personas = [
#     Alumno('Juan',23,[10,12,15,9]),
#     Profesor('Espejo','50','Matematicas'),
#     Alumno('Ronny',25,[20,19,15,19]),
#     Profesor('Lavalle','30','Redes')
# ]

# for persona in personas:
#     print(persona.description())


#* for persona in personas:
# *    if isinstance(persona, Alumno):
#  *       print(f"{persona.nombre} es un Alumno")
#   *  elif isinstance(persona, Profesor):
#    *     print(f"{persona.nombre} es un Profesor")
#     *print(persona.descripion())  # Aquí sigue funcionando el polimorfismo



# 🔹 Ejercicio: Sistema de Empleados y Estudiantes
# Crea un sistema donde haya Personas, Estudiantes y Empleados.
# Cada persona tiene un nombre y edad.

# Los Estudiantes tienen un listado de notas y pueden calcular su promedio.
# Los Empleados tienen un sueldo y pueden recibir un bono según su antigüedad.Si el empleado ha trabajado 5 años o más, recibe un bono del 10% de su salario.
# Si ha trabajado menos de 5 años, no recibe bono.
# Implementa polimorfismo para que todos puedan mostrar su información de manera personalizada.
# Agrega un método para saber si un estudiante aprobó y si un empleado recibe bono.


# class Persona():
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def descripcion(self):

#         return f'Nombre:{self.nombre}\nEdad:{self.edad}'
    

    
# class Estudiantes(Persona):
#     def __init__(self, nombre, edad, notas):
#         super().__init__(nombre, edad)

#         self.notas = notas
        

#     @property
#     def estado(self):


#         promedio = sum(self.notas) / len(self.notas)
        
#         if promedio >= 13:
#             return 'Aprovado'
#         else:
#             return 'Desaprovado'


       
        # return 'Aprobado' if (sum(self.notas) / len(self.notas)) >= 13 else 'Desaprobado'


#     def descripcion(self):
#         base = super().descripcion()
#         print('\nEstudiante')
#         return f'{base}\nNotas: {self.notas}\nEstado:{self.estado}' 


# class Trabajadores(Persona):
#     def __init__(self, nombre, edad, sueldo,tiempo):
#         super().__init__(nombre, edad)

#         self.sueldo = sueldo
#         self.tiempo = tiempo

#     @property
#     def tiempo_trabajador(self):

#         tiempo = self.tiempo

#         if tiempo > 5 :
#             return self.sueldo * 0.10 + self.sueldo
#         else:
#             return self.sueldo
#     # return self.sueldo * 1.10 if self.tiempo > 5 else self.sueldo

#     def descripcion(self):
#         base = super().descripcion()
#         print('\nTrabajador')
#         return f'{base}\nTiempo trabajado: {self.tiempo} anos\nSueldo Base:{self.sueldo}\nsuelto total:{self.tiempo_trabajador}'


# tipo_persona = [Estudiantes('Juan', 23,[5,6,3]),Trabajadores('Maria',40,1000,5)]

# for persona in tipo_persona:
#     print(persona.descripcion())
#     print('-'*30)




class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Nombre: {self.nombre}\nEdad: {self.edad}'


class Estudiante(Persona):
    def __init__(self, nombre, edad, notas):
        super().__init__(nombre, edad)
        self.notas = notas

    @property
    def promedio(self):
        """Calcula el promedio de notas con manejo de error si la lista está vacía"""
        try:
            return sum(self.notas) / len(self.notas)
        except ZeroDivisionError:
            return 0  # Si no hay notas, el promedio es 0

    @property
    def estado(self):
        """Retorna si el estudiante está aprobado o no"""
        return 'Aprobado' if self.promedio >= 13 else 'Desaprobado'

    def __str__(self):
        return f'{super().__str__()}\nNotas: {self.notas}\nPromedio: {self.promedio:.2f}\nEstado: {self.estado}'


class Trabajador(Persona):
    def __init__(self, nombre, edad, sueldo, tiempo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
        self.tiempo = tiempo

    @property
    def sueldo_total(self):
        """Calcula el sueldo total con bono si tiene más de 5 años"""
        return self.sueldo * 1.10 if self.tiempo > 5 else self.sueldo

    def __str__(self):
        return f'{super().__str__()}\nTiempo trabajado: {self.tiempo} años\nSueldo Base: {self.sueldo}\nSueldo Total: {self.sueldo_total}'


# Lista de personas (mezcla de estudiantes y trabajadores)
personas = [
    Estudiante('Juan', 23, [15, 14, 15]),
    Trabajador('Maria', 40, 1000, 6),
    Estudiante('Ana', 20, []),  # Caso con lista vacía para ver manejo de errores
    Trabajador('Carlos', 35, 1200, 4)
]

# Mostrar la información de cada persona
for persona in personas:
    print(persona)
    print('-' * 30)
