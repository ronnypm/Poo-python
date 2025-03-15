class Vehiculos():
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(f'Marca: {self.marca}\nModelo: {self.modelo}\nEn Marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nFrenando: {self.frena}')



class Furgoneta(Vehiculos):
    
    def carga(self,cargar):
        self.cargado = cargar

        if self.cargado:
            return 'La furgoneta esta cargada '
        else:
            return'La furgoneta no esta cargada'



class moto(Vehiculos):
    h_caballito = ''

    def caballito(self):
        self.h_caballito = 'voy haciendo el caballito'

    def estado(self):
        print(f'Marca: {self.marca}\nModelo: {self.modelo}\nEn Marcha: {self.enmarcha}\nAcelerando: {self.acelera}\nFrenando: {self.frena}\nEstado: {self.h_caballito}')


class VElectrico():
    def __init__(self):
        self.autonimia = 100

    def cargar_energia(self):

        self.cargando = True


class BElectrica(Vehiculos, VElectrico):
    pass


mi_moto = moto('Honda','CBR')
mi_moto.caballito()
mi_moto.estado()
print('//////////////////////////////')

mi_furgoneta = Furgoneta('Renault','Kango')
mi_furgoneta.arrancar()
mi_furgoneta.estado()
print(mi_furgoneta.carga(True))

print('///////////////////////////////')

mi_bicicleta = BElectrica('Orbea','hc1030')