class Coche():

    def desplazamiento(self):
        print('Me desplazo utlizando cuatro ruedad')


class Moto():

    def desplazamiento(self):
        print('Me desplazo utilizando dos ruedas')



class Camion():

     def desplazamiento(self):
        print('Me desplazo utilizando seis ruedas')



def desplazamiento_vehiculo(vehiculo):

    vehiculo.desplazamiento()



vehiculos = [Coche(),Moto(),Camion()]

for vehiculo in vehiculos:
    desplazamiento_vehiculo(vehiculo)

# mi_vehiculo = Camion()

# desplazamiento_vehiculo(mi_vehiculo)