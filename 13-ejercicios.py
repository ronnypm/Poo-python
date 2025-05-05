# Ejercicio: Sistema de Transporte 🚗🚌✈️
# Crea un sistema de clases para distintos medios de transporte.

# Clase base Transporte con:

# Atributos: marca, modelo, capacidad (número de pasajeros).

# Método __str__() para mostrar la información.

# Clases hijas Auto, Bus y Avion, cada una con:

# Auto: tiene un atributo adicional tipo (sedán, SUV, deportivo).

# Bus: tiene rutas (lista de paradas).

# Avion: tiene altitud_maxima (metros).

# Todos deben sobrescribir __str__() usando super().

# Crear objetos de cada tipo y mostrarlos en pantalla.

class Transporte():
    def __init__(self, marca, modelo, capacidad):
        self.marca = marca 
        self.modelo = modelo 
        self.capacidad = capacidad

    def __str__(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nCapacidad: {self.capacidad}'



class Auto(Transporte):
    def __init__(self, marca, modelo, capacidad, tipo):
        super().__init__(marca, modelo, capacidad)
        self.tipo = tipo

    def __str__(self):
        print('Auto')
        return f'{super().__str__()}\nCapacidad: {self.capacidad}'



class Bus(Transporte):
    def __init__(self, marca, modelo, capacidad, rutas):
        super().__init__(marca, modelo, capacidad)
        self.rutas = rutas

    def __str__(self):
        print('Bus')
        return f"{super().__str__()}\nRutas: {self.rutas}"



class Avion(Transporte):
    def __init__(self, marca, modelo, capacidad, altura_maxima):
        super().__init__(marca, modelo, capacidad)
        self.altura_maxima = altura_maxima
    def __str__(self):
        print('Avion')
        return f'{super().__str__()}\nCapacidad: {self.capacidad}'



transporte = [Auto('Toyota','Hilux',100, 'Sedan'),Bus('El chino', 'Camion grande', 50, 'La c'), Avion('Super','Bianca', 200, 150)]

for mi_transporte in transporte:
    print(mi_transporte)
    print('-' * 30)
