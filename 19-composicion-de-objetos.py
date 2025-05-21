# class Motor:
#     def arrancar(self):
#         return "Motor encendido"


# class Rueda:
#     def girar(self):
#         return "Rueda girando"


# class Auto:
#     def __init__(self):
#         self.motor = Motor()
#         self.rueda = Rueda()

#     def conducir(self):
#         encendido = self.motor.arrancar()
#         movimiento = self.rueda.girar()

#         return f'{encendido}. {movimiento}. En marcha'
    

# auto = Auto()
# print(auto.conducir())


# ----------------------------------------------------------

# class EmailSender:
#     def enviar(self, mensaje):
#         print(f'Enviando por correo: {mensaje}')


# class SmsSender:
#     def enviar(self, mensaje):
#         print(f'Enviando mensaje por {mensaje}')


# class Notificador:
#     def __init__(self, canal):
#         self.canal = canal

#     def notificacion(self,mensaje):
#         self.canal.enviar(mensaje)


# n1 = Notificador(EmailSender())
# n1.notificacion('Hola por email')

# n2 = Notificador(SmsSender())
# n2.notificacion('Hola por sms')



# class Cliente:
#     def __init__(self, nombre, celular):
#         self.nombre = nombre
#         self.celular = celular

#     def __str__(self):
#         return f'{self.nombre} - {self.celular}'


# class Prenda:
#     def __init__(self, tipo, descripcion):
#         self.tipo = tipo
#         self.descripcion = descripcion

#     def __str__(self):
#         return f'{self.tipo}: {self.descripcion}'


# class Orden:
#     def __init__(self, cliente, prendas, fecha_entrega):
#         self.cliente = cliente            # Composición
#         self.prendas = prendas            # Composición (lista de Prenda)
#         self.fecha_entrega = fecha_entrega

#     def mostrar_detalles(self):
#         print(f'Cliente: {self.cliente}')
#         print(f'Fecha de entrega: {self.fecha_entrega}')
#         print('Prendas:')
#         for prenda in self.prendas:
#             print(f' - {prenda}')


# class OrdenTeñido(Orden):  # Herencia
#     def __init__(self, cliente, prendas, fecha_entrega, color):
#         super().__init__(cliente, prendas, fecha_entrega)
#         self.color = color

#     def mostrar_detalles(self):
#         super().mostrar_detalles()
#         print(f'Color para teñido: {self.color}')



# cliente1 = Cliente("Lucía", "123456789")
# prendas = [
#     Prenda("Camisa", "Algodón blanca"),
#     Prenda("Pantalón", "Jean azul"),
# ]

# orden1 = OrdenTeñido(cliente1, prendas, "2025-05-30", "Negro")
# orden1.mostrar_detalles()



# Excepción personalizada
# class FondosInsuficientesError(Exception):
#     def __init__(self, saldo, monto):
#         super().__init__(f"No hay fondos suficientes. Saldo actual: ${saldo}, monto solicitado: ${monto}")

# # Clase Cuenta
# class CuentaBancaria:
#     def __init__(self, saldo_inicial):
#         self.saldo = saldo_inicial

#     def retirar(self, monto):
#         if monto > self.saldo:
#             raise FondosInsuficientesError(self.saldo, monto)
#         self.saldo -= monto
#         return f'Retiro exitoso. Nuevo saldo: ${self.saldo}'

# # Clase Cajero que usa composición (tiene una CuentaBancaria)
# class CajeroAutomatico:
#     def __init__(self, cuenta):
#         self.cuenta = cuenta  # Composición: el cajero tiene una cuenta

#     def realizar_retiro(self, monto):
#         try:
#             mensaje = self.cuenta.retirar(monto)
#             print(mensaje)
#         except FondosInsuficientesError as e:
#             print(f'Error: {e}')

# # Uso del sistema
# mi_cuenta = CuentaBancaria(1000)
# cajero = CajeroAutomatico(mi_cuenta)

# cajero.realizar_retiro(300)   # ✅ Retiro exitoso
# cajero.realizar_retiro(800)   # ❌ Saldo insuficiente




# Excepción personalizada
class StockInsuficienteError(Exception):
    def __init__(self, disponibles, solicitados):
        super().__init__(f"No hay stock suficiente. Disponibles: {disponibles}, Solicitados: {solicitados}")

# Clase Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        if cantidad > self.stock:
            raise StockInsuficienteError(self.stock, cantidad)
        self.stock -= cantidad
        return f"{cantidad} unidades de '{self.nombre}' vendidas. Stock restante: {self.stock}"


# Instanciamos un producto
producto = Producto("Auriculares", 50, 10)

# Hacemos la venta desde otro lugar del código
try:
    print(producto.vender(3))     # ✅ Éxito
    print(producto.vender(8))     # ❌ Error: No hay suficiente stock
except StockInsuficienteError as e:
    print(f"Error de stock: {e}")
except ValueError as e:
    print(f"Error de validación: {e}")
