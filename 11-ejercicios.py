# Ejercicio: Sistema de Gestión de Empleados 🚀
# Vas a crear una clase Empleado con los siguientes atributos y comportamientos:

# ✅ Atributos:

# nombre (string)

# sueldo_base (float)

# años_experiencia (int, no puede ser negativo)

# ✅ Métodos y propiedades:

# sueldo_total: Propiedad calculada que suma un bono del 10% si el empleado tiene más de 5 años de experiencia.

# impuesto: Propiedad calculada que descuenta el 8% del sueldo total si supera los 3000 soles.

# detalle_empleado(): Devuelve una descripción con todos los datos.


# class Empleado():
#     def __init__(self,nombre,sueldo_base,años_experiencia ):
#         self.nombre = nombre
#         self.sueldo_base = sueldo_base
#         self.años_experiencia = años_experiencia


#     @property
#     def sueldo_total(self):

#         return self.sueldo_base + (self.sueldo_base * 0.10) if self.años_experiencia > 5 else self.sueldo_base
    
#     @property
#     def impuesto(self):
        
#         return self.sueldo_total - (self.sueldo_total * 0.08) if self.sueldo_total > 3000 else self.sueldo_total
    

#     def __str__(self):
#         return f'Nombre: {self.nombre}\nSueldo: {self.sueldo_base}\naños de experiencia: {self.años_experiencia}'


# empleado = Empleado('Ronny',5500,7)
# print(empleado)
# print(f'Sueldo total:{empleado.sueldo_total}')
# print(f'Sueldo con impuesto incluido: {empleado.impuesto}')

# ---------------------------------------------------------------------
# Ejercicio 1: Clases y Métodos Básicos
# 🔹 Objetivo: Practicar clases, métodos y __str__.

# Instrucciones:
# Crea una clase Libro con los atributos titulo, autor y anio.

# Agrega un método descripcion() que devuelva una cadena con la información del libro.

# Sobreescribe __str__ para que al imprimir el objeto se muestre su descripción.

# Crea 3 instancias de Libro y muestra sus datos.



# class Libro():
#     def __init__(self,titulo,autor,anio):
#         self.titulo = titulo
#         self.autor = autor
#         self.anio = anio

    
#     def descripcion(self):

#         return f'Titulo: {self.titulo}\nAutor: {self.autor}\nAño: {self.anio}'
    
#     def __str__(self):
        
#         return self.descripcion()
    

# libro = Libro('Los versos satanicos','Ronny',1989)
# libro1 = Libro('La ciudad y los perro','Pisfil',1919)
# libro2 = Libro('el principito','murayari',1959)



# -----------------------------------------------------------------------

# Ejercicio 2: Herencia y Métodos Sobreescritos
# 🔹 Objetivo: Practicar herencia y cómo sobrescribir métodos.

# Instrucciones:
# Crea una clase Vehiculo con atributos marca, modelo y año.

# Agrega un método descripcion() que devuelva los datos del vehículo.

# Crea una subclase Auto que herede de Vehiculo, con un atributo extra puertas.

# Sobrescribe descripcion() en Auto para incluir la cantidad de puertas.

# Crea una subclase Moto que herede de Vehiculo, con un atributo extra cilindrada.

# Sobrescribe descripcion() en Moto para incluir la cilindrada.



# class vehiculo():
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano

    
#     def descripcion(self):
#         return f'Marca: {self.marca}\nModelo: {self.modelo}\nAño: {self.ano}'
    
# class Auto(vehiculo):
#     def __init__(self, marca, modelo, ano,puertas):
#         super().__init__(marca, modelo, ano)
        
#         self.puertas = puertas


#     def descripcion(self):
#         base = super().decripcion()

#         print(f'\nAuto')
#         return f'{base}\nPuertas: {self.puertas}'
    

# class Moto(vehiculo):
#     def __init__(self, marca, modelo, ano,cilindrada):
#         super().__init__(marca, modelo, ano)

#         self.cilindrada = cilindrada

    
#     def descripcion(self):
#         base = super().decripcion()

#         print(f'\nMoto')
#         return f'{base}\nCilindrada: {self.cilindrada}'
    
# vehiculo = [Auto('Toyota','Yaris',2022,4),Auto('Kia','Picanto',2025,4),Moto('Honda','Honda GL 125 ',2013,1899)]


# for mi_vehiculo in vehiculo:
#     print(mi_vehiculo.descripcion())
#     print('-' * 30)



# 🏗 Ejercicio: Sistema de Empleados
# Crea una clase Empleado con los atributos nombre, salario y cargo. Luego, crea dos clases hijas:
# 🔹 Gerente: tiene un atributo adicional departamento.
# 🔹 Operario: tiene un atributo adicional horas_extra.

# Cada clase debe tener un método descripcion() que muestre la información de manera clara. Usa polimorfismo para sobrescribir descripcion() en las clases hijas.

