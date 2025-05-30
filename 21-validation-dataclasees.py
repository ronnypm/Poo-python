from dataclasses import dataclass

# @dataclass
# class Usuario:
#     nombre:str
#     edad:int


#     def __post_init__(self):
#         if not self.nombre.strip():
#             raise ValueError('El nombre no puede estar vacio')
        
#         if self.edad < 0:
#             raise ValueError('La edad no puede ser nagativa')
        

# u_1 = Usuario('Lucia',30)
# u_2 = Usuario('',30)
# u_3 = Usuario('Carlos',-5)



# @dataclass
# class Producto:
#     nombre:str
#     precio:float


#     def __post_init__(self):
#         self.nombre = self.nombre.strip().title()

#         if self.precio <= 0:
#             raise ValueError('El precio debe ser mayor a cero.')
        
# p = Producto('  Laptop gamer', 4500)
# print(p)


from typing import Optional

# @dataclass
# class Cliente:
#     nombre: str
#     correo: Optional[str] = None


#     def __post_init__(self):
#         if self.correo and '@' not in self.correo:
#             raise ValueError('Correo invalido')
        

# c = Cliente('juan', 'Correo.com')
# print(c)



@dataclass
class Usuario:
    nombre: str
    correo: str
    edad: int


    def __post_init__(self):
        # 1. Validación de Vacío/Nulo (la más básica)
        if not self.correo: # Esto captura cadenas vacías y None (aunque el tipo str previene None)
            raise ValueError("El correo electrónico no puede estar vacío.")
        
        # 2. Validación de formato (solo si ya sabemos que no está vacío)
        if '@' not in self.correo:
            raise ValueError("El correo electrónico debe contener un símbolo '@'.")
        


        partes_correo = self.correo.split('@')
        if len(partes_correo) != 2 or '.' not in partes_correo[1]:
             raise ValueError("El correo electrónico debe tener un formato de dominio válido (ej. usuario@dominio.com).")


# --- Pruebas ---
print("--- Validaciones Separadas de Correo ---")

# Caso 1: Correo vacío
try:
    user = Usuario("Test1", "", 25)
    print(user)
except ValueError as e:
    print(f"Error (Caso 1 - Vacío): {e}")

print("-" * 30)

# Caso 2: Correo sin @
try:
    user = Usuario("Test2", "correo.invalido.com", 30)
    print(user)
except ValueError as e:
    print(f"Error (Caso 2 - Sin @): {e}")

print("-" * 30)

# Caso 3: Correo con @ pero sin dominio válido (ej. "a@b")
try:
    user = Usuario("Test3", "usuario@dominio", 35)
    print(user)
except ValueError as e:
    print(f"Error (Caso 3 - Dominio Inválido): {e}")

print("-" * 30)

# Caso 4: Correo válido
try:
    user = Usuario("Test4", "ejemplo@dominio.com", 40)
    print(f"Usuario creado: {user}")
except ValueError as e:
    print(f"Error (Caso 4 - Válido): {e}")