# Ejercicio: Sistema de Gestión de Empleados 🚀
# Vas a crear una clase Empleado con los siguientes atributos y comportamientos:

# ✅ Atributos:

# nombre (string)

# sueldo_base (float)

# años_experiencia (int, no puede ser negativo)

# ✅ Métodos y propiedades:

# sueldo_total: Propiedad calculada que suma un bono del 10% si el empleado tiene más de 5 años de experiencia.

# impuesto: Propiedad calculada que descuenta el 8% del sueldo total si supera los 3000 soles.

# detalle_empleado(): Devuelve una descripción con todos los datos.


# class Empleado():
#     def __init__(self,nombre,sueldo_base,años_experiencia ):
#         self.nombre = nombre
#         self.sueldo_base = sueldo_base
#         self.años_experiencia = años_experiencia


#     @property
#     def sueldo_total(self):

#         return self.sueldo_base + (self.sueldo_base * 0.10) if self.años_experiencia > 5 else self.sueldo_base
    
#     @property
#     def impuesto(self):
        
#         return self.sueldo_total - (self.sueldo_total * 0.08) if self.sueldo_total > 3000 else self.sueldo_total
    

#     def __str__(self):
#         return f'Nombre: {self.nombre}\nSueldo: {self.sueldo_base}\naños de experiencia: {self.años_experiencia}'


# empleado = Empleado('Ronny',5500,7)
# print(empleado)
# print(f'Sueldo total:{empleado.sueldo_total}')
# print(f'Sueldo con impuesto incluido: {empleado.impuesto}')

# ---------------------------------------------------------------------
# Ejercicio 1: Clases y Métodos Básicos
# 🔹 Objetivo: Practicar clases, métodos y __str__.

# Instrucciones:
# Crea una clase Libro con los atributos titulo, autor y anio.

# Agrega un método descripcion() que devuelva una cadena con la información del libro.

# Sobreescribe __str__ para que al imprimir el objeto se muestre su descripción.

# Crea 3 instancias de Libro y muestra sus datos.



# class Libro():
#     def __init__(self,titulo,autor,anio):
#         self.titulo = titulo
#         self.autor = autor
#         self.anio = anio

    
#     def descripcion(self):

#         return f'Titulo: {self.titulo}\nAutor: {self.autor}\nAño: {self.anio}'
    
#     def __str__(self):
        
#         return self.descripcion()
    

# libro = Libro('Los versos satanicos','Ronny',1989)
# libro1 = Libro('La ciudad y los perro','Pisfil',1919)
# libro2 = Libro('el principito','murayari',1959)



# -----------------------------------------------------------------------

# Ejercicio 2: Herencia y Métodos Sobreescritos
# 🔹 Objetivo: Practicar herencia y cómo sobrescribir métodos.

# Instrucciones:
# Crea una clase Vehiculo con atributos marca, modelo y año.

# Agrega un método descripcion() que devuelva los datos del vehículo.

# Crea una subclase Auto que herede de Vehiculo, con un atributo extra puertas.

# Sobrescribe descripcion() en Auto para incluir la cantidad de puertas.

# Crea una subclase Moto que herede de Vehiculo, con un atributo extra cilindrada.

# Sobrescribe descripcion() en Moto para incluir la cilindrada.



# class vehiculo():
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano

    
#     def descripcion(self):
#         return f'Marca: {self.marca}\nModelo: {self.modelo}\nAño: {self.ano}'
    
# class Auto(vehiculo):
#     def __init__(self, marca, modelo, ano,puertas):
#         super().__init__(marca, modelo, ano)
        
#         self.puertas = puertas


#     def descripcion(self):
#         base = super().decripcion()

#         print(f'\nAuto')
#         return f'{base}\nPuertas: {self.puertas}'
    

# class Moto(vehiculo):
#     def __init__(self, marca, modelo, ano,cilindrada):
#         super().__init__(marca, modelo, ano)

#         self.cilindrada = cilindrada

    
#     def descripcion(self):
#         base = super().decripcion()

#         print(f'\nMoto')
#         return f'{base}\nCilindrada: {self.cilindrada}'
    
# vehiculo = [Auto('Toyota','Yaris',2022,4),Auto('Kia','Picanto',2025,4),Moto('Honda','Honda GL 125 ',2013,1899)]


# for mi_vehiculo in vehiculo:
#     print(mi_vehiculo.descripcion())
#     print('-' * 30)



# 🏗 Ejercicio: Sistema de Empleados
# Crea una clase Empleado con los atributos nombre, salario y cargo. Luego, crea dos clases hijas:
# 🔹 Gerente: tiene un atributo adicional departamento.
# 🔹 Operario: tiene un atributo adicional horas_extra.

# Cada clase debe tener un método descripcion() que muestre la información de manera clara. Usa polimorfismo para sobrescribir descripcion() en las clases hijas.


# class Empleado():
#     def __init__(self, nombre, salario, cargo):
#         self.nombre = nombre
#         self.salario = salario
#         self.cargo = cargo
    
    
#     def __str__(self):
#         return f'Nombre:{self.nombre}\nSalario: {self.salario}\n{self.cargo}'

# class Gerente(Empleado):
#     def __init__(self, nombre, salario, cargo, departamento):
#         super().__init__(nombre, salario, cargo)

#         self.departamento = departamento

#     def __str__(self):
#         return f'{super().__str__()}\nDepartamento: {self.departamento}'
    

# class Operario(Empleado):
#     def __init__(self, nombre, salario, cargo, horas_extras):
#         super().__init__(nombre, salario, cargo)

#         self.horas_extras = horas_extras

#     def __str__(self):
#         return f'{super().__str__()}\nHoras extras: {self.horas_extras}'
    
# empleados = [
#     Gerente('Ronny',3000,'Gerente general','Gerencia'),
#     Operario('juan',1500,'Maquinista',4)
# ]


# for mis_empleados in empleados:
#     print(mis_empleados)
#     print('-' * 30)



# --------------------------------------------------------------------------

# combinaremos super() con @property.
# Ejercicio:
# 📌 Crea una clase base Persona con atributos nombre y edad. Luego, crea dos clases hijas: Profesor y Alumno.

# Profesor tendrá un atributo extra salario.

# Alumno tendrá un atributo extra notas (lista de calificaciones).

# Usa @property para calcular:

# En Profesor: un bono del 10% si tiene más de 5 años de experiencia.

# En Alumno: el promedio de notas.


# class Persona():
#     def __init__(self,nombre, edad):
#         self.nombre = nombre 
#         self.edad = edad 
        
    
#     def __str__(self):
#         return f'Nombre: {self.nombre}\nEdad: {self.edad}'
    
# class Profesor(Persona):
#     def __init__(self, nombre, edad,tiempo_trabajo,salario):
#         super().__init__(nombre, edad)

#         self.salario = salario
#         self.tiempo_trabajo = tiempo_trabajo


#     @property
#     def bono(self):

#         return self.salario + (self.salario * 0.10) if self.tiempo_trabajo > 5 else self.salario 


#     def __str__(self):
#         return f'{super().__str__()}\nSalario: {self.salario},\nExperiencia: {self.tiempo_trabajo}\nSueldo neto: {self.bono}'
    

# class Alumno(Persona):
#     def __init__(self, nombre, edad,notas):
#         super().__init__(nombre, edad)

#         self.notas = notas

#     @property
#     def promedio(self):


#         try:
#             return sum(self.notas)/len(self.notas)
#         except ZeroDivisionError:
#             return 0 
        
#     def estado(self):

#         return 'Aprobado' if self.promedio >=13 else 'Reprobado'

    
#     def __str__(self):
#         return f'{super().__str__()}\nNotas: {self.notas}\nPromedio: {self.promedio}\nEstado: {self.estado()}'
    

# personas = [
#     Profesor('Eduardo',65,10,3000),
#     Alumno('Juan',23,[15,17,2,19]),
#     Profesor('Jose',45,4,1000),
#     Alumno('Ronny',27,[11,4,2,19]),
#     Alumno('Alberto',17,[])
# ]



# for mis_personas in personas:
#     print(mis_personas)
#     print('-' * 30)




# ----------------------------------------------------------------------------

# 🔥 Ahora toca profundizar en super() y @property con más detalles.

# 🔹 Ejercicio:
# Crea una clase base CuentaBancaria con atributos titular y saldo. Luego, crea dos clases hijas:

# CuentaAhorro, que tiene un interés anual y un método para aplicar intereses.

# CuentaCorriente, que tiene un límite de sobregiro.

# Requisitos:
# ✅ Usar super() para heredar atributos.
# ✅ Usar @property para calcular el saldo con intereses en CuentaAhorro.
# ✅ Implementar un método en CuentaCorriente para verificar si se puede retirar dinero.


# class CuentaBancaria():
#     def __init__(self,titular, saldo):
#         self.titular = titular
#         self.saldo = saldo


# class CuentaAhorro(CuentaBancaria):
#     def __init__(self, titular, saldo,interes_anual, anos):
#         super().__init__(titular, saldo)

#         self.interes_anual = interes_anual
#         self.anos = anos

#     @property
#     def interes(self):

#         return self.saldo * self.interes_anual * self.anos


#     def __str__(self):
#         return f'{super().__str__()}\nTitular: {self.titular}\nsaldo: {self.saldo}\nInteres anula: {self.interes_anual}\nAños: {self.anos}\nInteres ganado: {self.interes}'


# class CuentaCorriente(CuentaBancaria):
#     def __init__(self, titular, saldo, limite_sobregiro):
#         super().__init__(titular, saldo)

#         self.limite_sobregiro = limite_sobregiro

#     def retirar(self,monto):
#         self.monto = monto
        
#         return self.saldo - monto



"""
🧩 Ejercicio 1: Contador de vocales
Escribe un programa que pida al usuario ingresar una palabra o frase.
El programa debe recorrer el texto y contar cuántas vocales contiene (a, e, i, o, u, sin importar si están en mayúscula o minúscula).

Requiere: bucle for, método .lower(), condicional if.
"""

# palabra = input('Ingrese una palabra: ').lower()
# contador = 0

# for letras in palabra:
#     if letras in ['a','e','i','o','u']:
#         contador += 1

# print(f'La palabra {palabra} contiene {contador} vocales')



"""
🧩 Ejercicio 2: Verificador de contraseña segura
Pide al usuario que ingrese una contraseña. Luego, evalúa si cumple las siguientes condiciones:

Tiene al menos 8 caracteres

Contiene al menos una letra mayúscula

Contiene al menos un número

Muestra un mensaje indicando si la contraseña es segura o no.

Requiere: métodos de string como .isupper(), .isdigit(), bucle for, condicionales if.
"""

# here write your code


# contraseña = input("Ingrese una contrasena: ")

# contador_mayusculas = 0
# contador_numeros = 0

# for letras in contrasena:
#     if letras.isupper(): 
#         contador_mayusculas += 1
#     if letras.isdigit():
#         contador_numeros += 1

# if len(contraseña) >= 8 and contador_mayusculas >= 1 and contador_numeros >= 1:
#     print('La contraseña es segura!')
# else:
#     print('La contraseña no es segura!')
    


       
        
"""
🧩 Ejercicio 3: Eco limitado
Solicita al usuario una palabra y un número. Luego imprime esa palabra tantas veces como el número indicado, una por línea.

Requiere: bucle for o while, entrada por teclado, impresión controlada.
"""

# here write your code


# Solucion con while

# palabra = input('Ingrese una palabra: ')
# numero = int(input('Ingrese una palabra: '))

# contador = 0

# while contador < numero:
#     print(palabra)
#     contador += 1


# print('-' * 30)

# # Solucion con for

# palabra = input('Ingrese una palabra: ')
# numero = int(input('Ingrese una palabra: '))

# for i in range(numero):
#     print(palabra)



"""
🧩 Ejercicio 4: Contador de letras por palabra
Solicita una frase al usuario. El programa debe recorrer la frase carácter por carácter y contar cuántas letras tiene cada palabra, ignorando los espacios.
Muestra el número de letras por palabra en orden.

Ejemplo:

Entrada: "Hola mundo Python"
Salida:
Palabra 1: 4 letras
Palabra 2: 5 letras
Palabra 3: 6 letras

Requiere: métodos de cadena como .split(), bucle for, condicional if.
"""

# here write your code


# frase = input('Ingrese una frase: ')
# palabra = frase.split()

# palabra.sort(key=len)


# for indice,letras in enumerate(palabra.sort()):
#     print(f'Palabra {indice + 1}: {len(letras)} letras')



