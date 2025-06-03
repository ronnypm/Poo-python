# from abc import ABC, abstractmethod


# class Figura(ABC):

#     @abstractmethod
#     def calcular_area(self):
#         pass


# class Rectangulo(Figura):
#     def __init__(self,ancho:int, alto:int):
#         self.ancho = ancho
#         self.alto = alto


#     def calcular_area(self):
#         return self.ancho * self.alto
    
# r = Rectangulo(4, 5)
# print(r.calcular_area())


from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


    @abstractmethod
    def moverse(self):
        pass


    def descripcion(self):
        return f'Vehiculo: {self.marca} Modelo:{self.modelo}'
    

class Coche(Vehiculo):
    def __init__(self, marca, modelo, tipo_combustible):
        super().__init__(marca, modelo)
        self.tipo_combustible = tipo_combustible


    def moverse(self):
        return f'Vehiculo: {self.marca} {self.modelo} se mueve usando {self.tipo_combustible}'
    

class Barco(Vehiculo):
    def __init__(self, marca, modelo, tipo_navegacion):
        super().__init__(marca, modelo)
        self.tipo_navegacion = tipo_navegacion

    def moverse(self):
        return f'El barco {self.marca} {self.modelo} se mueve por el agua usando {self.tipo_navegacion}'
    

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

mi_coche = Coche('Toyota', 'Corolla', 'Gasolina')
print(mi_coche.descripcion())
print(mi_coche.moverse())

print('-' * 30)
mi_barco = Barco('Yamaha', 'WaveryRunner', 'Helice')
print(mi_barco.descripcion())
print(mi_barco.moverse())