#  ¿Qué es herencia múltiple?
# En Python, una clase puede heredar de más de una clase base al mismo tiempo. Esto permite combinar comportamientos de múltiples fuentes en una sola clase.

# class Persona:

#     def indentidad(self):
#         return 'Soy una persona'
    

# class Trabajador:

#     def indentidad(self):
#         return'Soy un trabajador'
    

# class Empleado(Persona,Trabajador):
#     pass



# empleado  = Empleado()
# print(empleado.indentidad())


# help(empleado)


# class A:
#     def hablar(self):
#         return 'A dice hola.'

# class B:
#     def hablar(self):
#         return 'B dice hola.'

# class C(A,B):
#     pass

# c = C()
# print(c.hablar())






# class A:
#     def saludar(self):
#         print('Hola desde A.')
#         super().saludar()

# class B:
#     def saludar(self):
#         print('Hola desde B.')

# class C(A,B):
#     def saludar(self):
#         print('Hola desde C')
#         super().saludar()

# class D(C):
#     def saludar(self):
#         print('Hola desde D')
#         super().saludar()

# class Base():
#     def saludar(self):
#         print('Hola desde Base')


# d = D()
# d.saludar()
# help(d)





# class Usuario:
#     def __init__(self, nombre):
#         self.nombre = nombre

#     def info(self):
#         print(f"Usuario: {self.nombre}")


# class RolAdmin:
#     def permisos(self):
#         print("Permisos: Puede crear, editar y eliminar usuarios.")

#     def acceder_panel_admin(self):
#         print("Accediendo al panel de administración...")


# class RolCliente:
#     def permisos(self):
#         print("Permisos: Puede comprar productos.")

#     def hacer_compra(self):
#         print("Realizando compra...")


# # Herencia múltiple: un usuario puede ser Admin y Cliente a la vez
# class UsuarioEspecial(Usuario, RolAdmin, RolCliente):
#     def mostrar_permisos(self):
#         self.permisos()  # Aquí se aplica el MRO


# usuario1 = UsuarioEspecial("Ronny")

# usuario1.info()                 # Muestra nombre
# usuario1.mostrar_permisos()     # ¿Admin o Cliente?
# usuario1.acceder_panel_admin()  # Método de RolAdmin
# usuario1.hacer_compra()         # Método de RolCliente

# print(UsuarioEspecial.__mro__)  # Ver MRO

# help(usuario1)






class MixinExportable:
    def exportar(self, formato="excel"):
        formatos_disponibles = {
            "excel": self._exportar_excel,
            "pdf": self._exportar_pdf,
            "csv": self._exportar_csv
        }

        if formato not in formatos_disponibles:
            raise ValueError(f"Formato no soportado: {formato}")
        
        return formatos_disponibles[formato]()

    def _exportar_excel(self):
        return "Exportando como Excel..."

    def _exportar_pdf(self):
        return "Exportando como PDF..."

    def _exportar_csv(self):
        return "Exportando como CSV..."

# Clase principal
class Reporte:
    def generar(self):
        return "Generando reporte..."

# Combinamos funcionalidad base + mixin
class ReporteFinal(Reporte, MixinExportable):
    pass

# 🎯 Uso:
reporte = ReporteFinal()
print(reporte.generar())                # "Generando reporte..."
print(reporte.exportar("excel"))        # "Exportando como Excel..."
print(reporte.exportar("pdf"))          # "Exportando como PDF..."
print(reporte.exportar("csv"))          # "Exportando como CSV..."
# print(reporte.exportar("xml"))        # Levanta error: formato no soportado
