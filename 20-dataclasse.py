# 🧳 Analogía de la vida real: Una ficha de registro
# Imagina que vas a una consulta médica. Te dan una ficha donde solo hay que registrar tu nombre, edad, y DNI. Nadie espera que esa ficha haga cosas: solo guarda datos. No necesita métodos complejos, ni lógica de negocio. Solo necesita existir y ser clara.

# Eso mismo hacen las dataclasses en Python: permiten crear clases que son solo “fichas” para guardar datos, de forma clara, elegante y sin escribir mucho código repetitivo.



from dataclasses import dataclass

@dataclass 
class Usuario:
    nombre: str
    edad: int
    activo: bool = True

u_1 = Usuario('Ronny',25,False)
u_2 = Usuario('Genearo',65)
print(u_1)
print(u_1 == u_2)
print(u_1.nombre)
    