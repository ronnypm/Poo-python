class SinNotasError(Exception):
    def __init__(self, mensaje="El estudiante no tiene notas registradas."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.notas = []

    def agregar_nota(self, nota):
        if 0 <= nota <= 20:
            self.notas.append(nota)
        else:
            print(f"❌ Nota inválida: {nota}. Debe estar entre 0 y 20.")

    def promedio(self):
        if not self.notas:
            raise SinNotasError()
        return sum(self.notas) / len(self.notas)

    def __str__(self):
        try:
            promedio = self.promedio()
        except SinNotasError as e:
            promedio = e.mensaje
        return f'Nombre: {self.nombre}\nEdad: {self.edad}\nPromedio: {promedio}'



ronny = Estudiante("Ronny", 29)

# ronny.promedio()  # Si lo descomentás, lanza una excepción

ronny.agregar_nota(18)
ronny.agregar_nota(19)

print(ronny)
