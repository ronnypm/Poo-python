# • Clase:Modelo donde se redactan las caracteristicas comunes de un grupo de objetos

# ejemplar de clase/ inistancia / objeto de clase son sinonimo estos pertenecen a una clase 

#encapculacion 

# class Coche(): #!clase
#     def __init__(self):
#         self.__largo_chasis = 250
#         self.__ancho_chasis = 120          #!atrobutos o estado
#         self.__ruedas = 4
#         self.__enmarcha = False

#     def arrancar(self,arrancamos):  #!comportamiento/metodo
        
#             self.__enmarcha = arrancamos
        
#             if self.__enmarcha:
#                 return 'El auto esta en la carretera'
#             else:
#                 return 'El auto esta parado'


#     def estado(self):

#             print(f'El auto tiene un largo de {self.__largo_chasis}, ancho {self.__ancho_chasis} y {self.__ruedas} ruedas' )

# mi_coche = Coche()  #!objeto /instancia de clase/emplemparisar una clase
# print(mi_coche.arrancar(True))
# mi_coche.estado()




class Empleado:
    empresa = 'Sastreria Itham'

    def __init__(self, nombre):
        self.nombre = nombre

e1 = Empleado('Lucia')
e2 = Empleado('Juan')

print(e1.empresa)
print(e2.empresa)
Empleado.empresa = 'Murayaritech'
print(e1.empresa)












