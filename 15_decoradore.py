class CuentaBancaria:
    # Atributos estáticos (si los tuviéramos)
    tipo_cuenta = "Ahorros"
    
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    @property
    def saldo(self):
        return self.__saldo  # Getter

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print("El saldo no puede ser negativo.")
        else:
            self.__saldo = valor  # Setter

    @staticmethod
    def calcular_intereses(saldo):
        # Método estático que calcula el interés de un saldo dado (5% anual)
        return saldo * 0.05

    def __str__(self):
        return f"Cuenta de {self.titular} - Saldo: {self.saldo} - Tipo: {self.tipo_cuenta}"

# Crear una cuenta
cuenta = CuentaBancaria("Carlos", 1000)

# Usar el getter y setter
print(cuenta.saldo)  # Imprime 1000
cuenta.saldo = 1200  # Modifica el saldo
print(cuenta.saldo)  # Imprime 1200

# Calcular los intereses de la cuenta
print("Intereses:", CuentaBancaria.calcular_intereses(cuenta.saldo))  # Imprime 60.0

# Imprimir la cuenta, invoca automáticamente __str__
print(cuenta)  # Imprime: Cuenta de Carlos - Saldo: 1200 - Tipo: Ahorros