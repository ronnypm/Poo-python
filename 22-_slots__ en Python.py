# class Persona:
#     __slots__ = ('nombre', 'edad')

#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

# persona = Persona('Pisfil', 23)
# print(persona.nombre, persona.edad)


# class Coordenada:
#     __slot__ = ('latitud', 'longitud')


#     def __init__(self, lat, lon):
#         self.latitud = lat
#         self.longitud = lon

    
#     def __str__(self):
#         return f'Latitud: {self.latitud}\nLongitud: {self.longitud}'


# ubicacion_casa = Coordenada(12.345, -67.890)
# ubicacion_trabajo = Coordenada(12.360, -67.900)

# print(ubicacion_casa)
# print(ubicacion_trabajo)
# print(f"Casa-Longitud {ubicacion_casa.longitud}")
# print(f'Trabajo-Latitud {ubicacion_casa.latitud}')


# import sys

# class Persona:
#     def __init__(self, nombre):
#         self.nombre = nombre



# class PersonaCompacta:
#     __slots__ = ('nombre')

#     def __init__(self, nombre):
#         self.nombre = nombre

# p1 = Persona('Lucia')
# p2 = PersonaCompacta('Lucia')

# print(sys.getsizeof(p1))
# print(sys.getsizeof(p2))

from dataclasses import dataclass

@dataclass(slots=True)
class Producto:
    nombre: str
    precio: float