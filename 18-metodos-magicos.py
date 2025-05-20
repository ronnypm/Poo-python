class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Persona: {self.nombre}"

    def __repr__(self):
        return f"Persona('{self.nombre}')"

p = Persona("Lucía")
print(p)      # usa __str__: Persona: Lucía
print(repr(p))      # usa __str__: Persona: Lucía
        # en consola usa __repr__: Persona('Lucía')
# -------------------------------------------------------------------------
# metodo __len__

# class Biblioteca:
#     def __init__(self, libros):
#         self.libros = libros

#     def __len__(self):
#         return len(self.libros)


# b = Biblioteca(["1984", "El Principito", "Matar a un ruiseñor"])
# print(len(b))  # Salida: 3
# # --------------------------------------------------------------------------------

# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def __repr__(self):
#         return f"{self.nombre} ({self.edad} años)"

#     def __eq__(self, other):
#         return self.edad == other.edad

#     def __lt__(self, other):
#         return self.edad < other.edad

#     def __gt__(self, other):
#         return self.edad > other.edad

# p1 = Persona("Lucía", 25)
# p2 = Persona("Dante", 30)
# p3 = Persona("Lucía", 25)

# print(p1 == p2)  # False
# print(p1 == p3)  # True
# print(p1 < p2)   # True
# print(p2 > p3)   # True



# ¡Exactamente!
# Los métodos mágicos __lt__ y __gt__ significan lo siguiente:

# __lt__ → "less than" → menor que (<)

# __gt__ → "greater than" → mayor que (>)

# Y también hay otros relacionados:

# Método	Significado	Operador
# __eq__	equal	==
# __ne__	not equal	!=
# __lt__	less than	<
# __le__	less than or equal	<=
# __gt__	greater than	>
# __ge__	greater or equal	>=

# Si querés, puedo darte un ejemplo práctico usando varios de estos. ¿Te gustaría comparar objetos tipo Producto, Jugador, Libro, etc.?