# 🧠 ¿Qué es la abstracción?
# En programación orientada a objetos, la abstracción es el proceso de definir una interfaz clara para interactuar con un objeto, ocultando los detalles de implementación que no son necesarios para el exterior.

# En otras palabras: separamos el “qué hace” del “cómo lo hace”.



# class TarjetaBancaria:
#     def __init__(self,saldo_inicial):
#         self.__saldo = saldo_inicial

#     def consultar_saldo(self):
#         return f'Tu saldo es S/{self.__saldo: .2f}'
    
#     def retirar(self, monto):
#         if monto <= 0:
#             return 'El monto debe ser positivo'
#         if monto > self.__saldo:
#             return 'Fondos insuficientes'
#         self.__saldo -= monto
#         return f'Retiro exitoso. Saldo restante: S/{self.__saldo: .2f}'
    
# tarjeta = TarjetaBancaria(1000)
# print(tarjeta.consultar_saldo())
# print(tarjeta.retirar(200))
# print(tarjeta.__saldo)
         

from abc import ABC,abstractmethod

#clase abstracta(Abstraccion)

class Cuenta(ABC):
    @abstractmethod
    def consultar_saldo(self):
        pass

    @abstractmethod
    def retirar(self):
        pass


#clase concreta que hereda de cuenta

class TarjetaBancaria(Cuenta):
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    
    def consultar_saldo(self):
        return f'Tu saldo es S/{self.__saldo:.2f}'
    

    def retirar(self,monto):
        
        if monto <= 0:
            return f'El monto debe ser positivo'
        if monto > self.__saldo:
            return f'Saldo insuficiente'
        self.__saldo -= monto
        return f'Retiro exitoso. Saldo restante: S/{self.__saldo:.2f}'
        

tarjeta = TarjetaBancaria(1000)
print(tarjeta.consultar_saldo())
print(tarjeta.retirar(300))
print(tarjeta.consultar_saldo())