class Personaje():
    def __init__(self,nombre,fuerza,inteligencia,defensa,vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida 


    def atributo(self):

        print('Datos del Personaje\n')
        print(f'El nombre del jugador es: {mi_personaje.nombre}')
        print(f'La fuerza del jugador es: {mi_personaje.fuerza}')
        print(f'La inteligencia del jugador es: {mi_personaje.inteligencia}')
        print(f'La defensa del jugador es: {mi_personaje.defensa}')
        print(f'La vidad del jugador es: {mi_personaje.vida}')
    

    def subir_nivel(self,fuerza,inteligencia,defensa):

        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa


    def estar_vivo(self):

       return self.vida > 0
    

    def morir(self):

        self.vida = 0
        print(f'{self.nombre} ha muerto')


    def dano(self, enemigo):
        return self.fuerza - enemigo.defensa


    def atacar(self,enemigo):

        dano = self.dano(enemigo) 
        enemigo.vida = enemigo.vida - dano
        print(f'{self.nombre} ha realizado {dano} puntos de dano a {enemigo.nombre}')     
        print(f'La vida de {enemigo.nombre} es, {enemigo.vida}')     

mi_personaje = Personaje('Ronny',10,1,5,100)
mi_enemigo = Personaje('Enemigo malo',8,7,3,100)
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributo()