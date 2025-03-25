#  ¿Qué es __str__ en Python?
# Es un método especial que se usa para definir cómo se representa un objeto cuando lo conviertes en cadena de texto (con str(objeto)) o cuando lo imprimes (print(objeto)).

# class Persona():
#     def __init__(self, nombre,edad):
#         self.nombre = nombre
#         self.edad = edad

#     def __str__(self):
#         return f'{self.nombre} tiene {self.edad} años de edad'
    
# Ronny = Persona('Ronny', 25)
# print(Ronny) # Ronny tiene 25 años de edad
# ¿Qué es __repr__ en Python? 
# Es un método especial que se usa para definir cómo se representa un objeto cuando lo imprimes en la consola (sin usar print(objeto)).
#
# class Persona():
#     def __init__(self, nombre, edad):    
#         self.nombre = nombre
#         self.edad = edad

#     def __repr__(self):
#         return f'Persona({self.nombre}, {self.edad})'

# Ronny = Persona('Ronny', 25)
# print(Ronny) # Persona(Ronny, 25)
# ¿Cuál es la diferencia entre __str__ y __repr__?
# La diferencia principal es que __str__ se llama cuando imprimes un objeto con print(objeto) o str(objeto), mientras que __repr__ se llama cuando imprimes un objeto en la consola sin usar print(objeto).
#
# ¿Cuándo deberías usar __str__ y __repr__?
# __str__ se usa para representar un objeto de forma amigable para el usuario final, mientras que __repr__ se usa para representar un objeto de forma detallada para el desarrollador.
#
# ¿Qué pasa si solo implementas __str__ y no __repr__?
# Si solo implementas __str__, Python usará __str__ como una copia de __repr__.


#
# ¿Qué pasa si solo implementas __repr__ y no __str__?
# Si solo implementas __repr__, Python usará __repr__ para ambos casos.


# ¿Qué es __len__ en Python?                
# Es un método especial que se usa para definir la longitud de un objeto cuando usas la función len(objeto).
#
# class Lista():
#     def __init__(self, elementos):
#         self.elementos = elementos

#     def __len__(self):
#         return len(self.elementos)

# mi_lista = Lista([1, 2, 3, 4, 5])
# print(len(mi_lista)) # 5
#------------------------------------------------------------------

# Ejercicio 1
# Crea una clase Libro con los atributos titulo y autor. Implementa el método __str__ para que al imprimir un objeto de esta clase, muestre el título y el autor en formato:


# class Libro():
#     def __init__(self,titulo,autor):
#         self.titulo = titulo
#         self.autor = autor

#     def __str__(self):
#         return f'{self.titulo} de {self.autor}'
    
# libro = Libro('Los versos satánicos', 'Salman Rushdie')
# print(libro) # Los versos satánicos de Salman Rushdie


# Ejercicio 2
# Crea una clase Persona con los atributos nombre y edad. Implementa el método __str__ para que al imprimir un objeto de esta clase, muestre la información en este formato:


# class Persona():
#     def __init__(self,nombre,edad):
#         self.nombre = nombre
#         self.edad = edad


#     def __str__(self):
#         return f'{self.nombre} tiene {self.edad}'
    
    
# persona = Persona('Ronny',27)
# print(persona)


# class Car():
#     def __init__(self,brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
        
#     def __str__(self):
#         return f'Marca:{self.brand}\nModelo:{self.model}\nano{self.year}'
    
# car = Car('Toyota','Corolla',2025)
# print(car)