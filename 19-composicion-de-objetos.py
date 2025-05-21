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



class Cliente:
    def __init__(self, nombre, celular):
        self.nombre = nombre
        self.celular = celular

    def __str__(self):
        return f'{self.nombre} - {self.celular}'


class Prenda:
    def __init__(self, tipo, descripcion):
        self.tipo = tipo
        self.descripcion = descripcion

    def __str__(self):
        return f'{self.tipo}: {self.descripcion}'


class Orden:
    def __init__(self, cliente, prendas, fecha_entrega):
        self.cliente = cliente            # Composición
        self.prendas = prendas            # Composición (lista de Prenda)
        self.fecha_entrega = fecha_entrega

    def mostrar_detalles(self):
        print(f'Cliente: {self.cliente}')
        print(f'Fecha de entrega: {self.fecha_entrega}')
        print('Prendas:')
        for prenda in self.prendas:
            print(f' - {prenda}')


class OrdenTeñido(Orden):  # Herencia
    def __init__(self, cliente, prendas, fecha_entrega, color):
        super().__init__(cliente, prendas, fecha_entrega)
        self.color = color

    def mostrar_detalles(self):
        super().mostrar_detalles()
        print(f'Color para teñido: {self.color}')



cliente1 = Cliente("Lucía", "123456789")
prendas = [
    Prenda("Camisa", "Algodón blanca"),
    Prenda("Pantalón", "Jean azul"),
]

orden1 = OrdenTeñido(cliente1, prendas, "2025-05-30", "Negro")
orden1.mostrar_detalles()
