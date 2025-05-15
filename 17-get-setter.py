# class Producto:
#     def __init__(self, nombre, precio):
#         self.nombre = nombre
#         self._precio = precio


#     @property
#     def precio(self):
#         print('Opteniendo precio....')
#         return self._precio
    

#     @precio.setter
#     def precio(self, nuveo_preccio):
#         if nuveo_preccio < 0:
#             raise ValueError('El precio no puede ser negativo')
#         print('Asignando nuevo precio....')
#         self._precio = nuveo_preccio
    

# p = Producto('Laptop', 3000)
# print(p.precio)
# p.precio -= 10
# print(p.precio)




# 🧭 Bonus: propiedad de solo lectura

# class Usuario:
#     def __init__(self, nombre):
#         self._nombre = nombre

#     @property
#     def nombre(self):
#         return self._nombre
    
# u = Usuario('Lucia')
# print(u.nombre)

# u.nombre = 'Ronny'


class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return round(self._saldo, 2)

    @saldo.setter
    def saldo(self, nuevo_valor):
        if nuevo_valor < 0:
            # raise ValueError("Saldo no puede ser negativo")
            self._saldo = nuevo_valor


cuenta = Cuenta(100.24424)
cuenta.saldo = -300
print(cuenta.saldo)