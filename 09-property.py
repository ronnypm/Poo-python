# Usé @property porque me permite calcular valores en tiempo real sin almacenarlos. Así evito datos desactualizados, hago el código más limpio y flexible, y me aseguro de que el resultado siempre sea correcto sin recalcularlo manualmente.



# @property reemplaza un atributo normal con una función que se ejecuta automáticamente al acceder al valor, permitiendo calcularlo en tiempo real en lugar de almacenarlo en memoria. Esto hace que el dato siempre esté actualizado, sin desperdiciar recursos ni requerir modificaciones manuales.


# class Empleado():
#     def __init__(self, nombre, sueldo_mensual):
#         self.nombre = nombre
#         self.sueldo_mensual = sueldo_mensual
        
#     @property
#     def Sueldo_anual(self):
#         return self.sueldo_mensual * 12
    
# mi_empleado = Empleado('Juan', 1000)
# print(mi_empleado.Sueldo_anual)
   

#  Ejemplo 2: Cálculo de área en tiempo real
# Si tenemos una clase Rectangulo, podemos calcular el área dinámicamente en función de ancho y alto:



# class Rectangulo():
#     def __init__(self, ancho, altura):
#         self.ancho = ancho
#         self.altura = altura
        
#     @property
#     def area(self):
#         return self.ancho * self.altura #Se calcula en tiempo real
    
# mi_rectangulo = Rectangulo(3,4)
# print(mi_rectangulo.area)

# mi_rectangulo.ancho = 5
# print(mi_rectangulo.area)


# 🔹 Ejemplo 3: Edad calculada a partir del año de nacimiento

# from datetime import datetime

# class Persona():
#     def __init__(self, nombre, año_nacimiento):
#         self.nombre = nombre
#         self.año_nacimiento = año_nacimiento
        
#     @property
#     def edad(self):
#         return datetime.now().year - self.año_nacimiento #Se calcula en tiempo real
    
# mi_persona = Persona('Juan', 1996)
# print(mi_persona.edad)

# mi_persona.año_nacimiento = 2004
# print(mi_persona.edad)


# 🔹 Ejemplo 4: Precio con impuestos

# class Producto():
#     def __init__(self, nombre, precio_base, impuesto = 0.15):
#         self.nombre = nombre
#         self.precio_base = precio_base
#         self.impuesto = impuesto
        
#     @property
#     def precio_final(self):
#         return self.precio_base * (1 + 0.15) #Se calcula en tiempo real
    
# mi_producto = Producto('Laptop', 1000)
# print(mi_producto.precio_final)

# mi_producto.precio_base = 1200
# print(mi_producto.precio_final)





#  Ejemplo 5: Estado de carga de una batería
# Si tenemos un objeto que representa la batería de un dispositivo, podemos calcular el estado en función del porcentaje de carga:


class Bateria():
    def __init__(self, porcentaje_carga):
        self.porcentaje_carga = porcentaje_carga
        
    @property
    def estado(self):
        if self.porcentaje_carga == 100:
            return 'Completamente cargada'
        elif self.porcentaje_carga > 75:
            return 'Cargada'
        elif self.porcentaje_carga > 50:
            return 'Medio'
        elif self.porcentaje_carga > 25:
            return 'Baja'
        else:
            return 'Muy baja'
        

mi_bateria = Bateria(100)
print(mi_bateria.estado)    

mi_bateria.porcentaje_carga = 10
print(mi_bateria.estado)