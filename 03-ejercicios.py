# Ejercicio 1: Mascotas y Perros 🐶
# Crea una clase base Mascota con un método hacer_sonido(), y una clase Perro que herede de Mascota y sobrescriba el método para que diga "¡Guau guau!".

# 🔹 Objetivo
# Definir una clase base con un método.
# Crear una clase hija que sobrescriba ese método.



# class Mascota():
#     def __init__(self,nombre):
#         self.nombre = nombre

#     def hacer_sonido():
#         return 'Hace gua, gua.....'

# class Perro(Mascota):

#     def hacer_sonido(self):
#         return 'Hace gua, gua.....'
    

# mi_perro = Perro('Kratos')
# print(mi_perro.nombre)
# print(mi_perro.hacer_sonido())





# Ejercicio 2: Dispositivos Electrónicos 📱💻
# Crea una clase Dispositivo con atributos marca y modelo. Luego, crea dos clases Telefono y Laptop que hereden de Dispositivo.

# 🔹 Objetivo
# Aplicar herencia básica.
# Agregar un método adicional en cada subclase.


# class Dispositivo():
#     def __init__(self,marca, modelo):
#         self.marca = marca
#         self.modelo = modelo

#     def info(self):
#         return f'Marca: {self.marca}, Modelo: {self.modelo}'

# class Telefono(Dispositivo):
#     def llamar(self):
#         return f'EL telefono marca {self.marca},modelo {self.modelo} llamando'

# class Laptop(Dispositivo):
#     def encender(self):
#         return f'La laptop marca {self.marca},modelo {self.modelo} esta encendida'


# mi_telefono = Telefono('Samsung','Galaxy s23')
# print(mi_telefono.llamar())

# mi_laptop = Laptop('Dell','ACM1P')
# print(mi_laptop.encender())



# Ejercicio 1: Herencia y Métodos Personalizados
# Crea una clase base Animal con un método hacer_sonido(), y luego define dos clases Perro y Gato que hereden de Animal. Cada una debe tener su propio sonido al ejecutar hacer_sonido().

# Objetivo: Practicar la herencia y la personalización de métodos en las subclases.

# Aquí tienes la estructura base, pero trata de completarla tú mismo:



# class Animal:
#     def __init__(self, nombre):
#         self.nombre = nombre

#     def hacer_sonido():
#         return 'Sonido generico de un animal'

# class Perro(Animal):
#     def hacer_sonido(self):
#         return f'{self.nombre} dice guau, guauuuu...!'

# class Gato(Animal):
#     def hacer_sonido(self):
#         return f'{self.nombre} dice miau, miauuuu...!'


# mi_perro = Perro('Kratos')
# print(mi_perro.hacer_sonido())


# mi_gato = Gato('Copernico')
# print(mi_gato.hacer_sonido())


# Ejercicio: Vehículos 🚗🚲🛵
# Vamos a crear una jerarquía de clases para representar diferentes tipos de vehículos.

# Requerimientos:
# Crea una clase Vehiculo con:

# Un constructor (__init__) que reciba marca y modelo.
# Un método info() que devuelva la marca y modelo del vehículo.
# Crea dos clases que hereden de Vehiculo:

# Auto: Agrega un método conducir() que devuelva un mensaje diciendo que el auto está en movimiento.
# Bicicleta: Agrega un método pedalear() que devuelva un mensaje diciendo que la bicicleta está en movimiento.
# Crea instancias de ambas clases y llama a sus métodos.


# class Vehicle():
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model 
#         self.status = False

#     def info(self):
#         return f'Brand: {self.brand}\nModel: {self.model}'
    

# class Car(Vehicle):
#     def drive(self, moving):
#         self.status = moving
#         return 'The car is moving' if self.status else 'The car is stopped'
            

# class Bicycle(Vehicle):
#     def pedal(self, moving):
#         self.status = moving
#         return 'The bicycle is moving' if self.status else 'The bicycle is stopped'


# my_car = Car('Toyota', 'Yaris')
# my_bicycle = Bicycle('Trek', 'FX 3 Disc')

# print(my_car.info())
# print(my_car.drive(True))
# print(my_bicycle.info())
# print(my_bicycle.pedal(False))


# Crea una clase InstrumentoMusical con un atributo nombre y un método tocar(), que devuelva "Sonido del instrumento". Luego, crea dos clases Guitarra y Piano que hereden de InstrumentoMusical y sobrescriban el método tocar(), devolviendo "Rasgueo de guitarra" y "Notas de piano", respectivamente.

# Traducción en inglés:
# Create a class MusicalInstrument with an attribute name and a method play(), which returns "Sound of the instrument". Then, create two classes Guitar and Piano, which inherit from MusicalInstrument and override the play() method to return "Guitar strumming" and "Piano notes", respectively.

class Musical_instrument():
    def __init__(self,name):
        self.name = name

    def play(self):
        return 'sound of the instrument'
    
class Guitar(Musical_instrument):
    def play(self):
        r

class piano(Musical_instrument):
    pass