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

class EmailSender:
    def enviar(self, mensaje):
        print(f'Enviando por correo: {mensaje}')


class SmsSender:
    def enviar(self, mensaje):
        print(f'Enviando mensaje por {mensaje}')


class Notificador:
    def __init__(self, canal):
        self.canal = canal

    def notificacion(self,mensaje):
        self.canal.enviar(mensaje)


n1 = Notificador(EmailSender())
n1.notificacion('Hola por email')

n2 = Notificador(SmsSender())
n2.notificacion('Hola por sms')