# Ejercicio
# Agrega un método a la clase Empleado llamado calcular_bono(), que determine un bono basado en la antigüedad del empleado.

# Si la antigüedad es menor a 5 años, el bono es el 5% del salario.
# Si la antigüedad es entre 5 y 10 años, el bono es el 10% del salario.
# Si la antigüedad es mayor a 10 años, el bono es el 15% del salario.
# Luego, dentro del método descripcion(), muestra también el bono calculado.


# class Persona():
    
#     def __init__(self,nombre, edad, lugar_residencia):
#         self.nombre = nombre
#         self.edad = edad
#         self.lugar_residencia = lugar_residencia


#     def descripcion(self):
#         print('Datod de usuario:')
#         print(f'Nombre:{self.nombre}\nEdad:{self.edad}\nLugar de residencia:{self.lugar_residencia}')


# class Empleado(Persona):

#     def __init__(self,salario,antiguedad, nombre, edad, lugar_residencia):
#         super().__init__(nombre, edad, lugar_residencia)
#         self.salario = salario
#         self.antiguedad = antiguedad


#     def calcular_bono(self):
#         if self.antiguedad < 5:
#             return self.salario * 0.05
#         elif self.antiguedad <=10:
#             return self.salario * 0.10
#         else:
#             return self.salario * 0.15

#     def descripcion(self):
#         super().descripcion()

#         print(f'Salario:{self.salario}\nAntiguedad:{self.antiguedad} años\nBono:{self.calcular_bono()}')


# mi_empleado = Empleado(1000,14,'Juan',24,'Lima')
# mi_empleado.descripcion()





# Ejercicio
# Crea una clase Estudiante que herede de Persona y agregue lo siguiente:

# Un atributo calificaciones, que será una lista de notas.
# Un método promedio(), que calcule el promedio de sus calificaciones.
# Un método descripcion(), que muestre la información del estudiante e indique si aprobó o reprobó.
# Si el promedio es mayor o igual a 11, el estudiante aprueba.
# Si es menor a 11, el estudiante reprueba.


# class Person():
#     #creation of the contruction of the Person class
#     def __init__(self,name, age, place_residence):
#         self.name = name
#         self.age = age 
#         self.place_residence = place_residence

#     def description(self):
#         print(f'Name: {self.name}\nAge:{self.age}\nPlace of the residence:{self.place_residence}')

# class student(Person):
#     def __init__(self, name, age, place_residence,gredes):
#         super().__init__(name, age, place_residence)
#         self.grades = gredes

#     def average(self):

#         return sum(self.grades)/ len(self.grades)

    
#     def  description(self):
#         super().description()

#         average = self.average()
#         status = 'Passed' if average >=13 else 'failed'
#         print(f'the averege is:{average:.2f}\nStatus:{status}')

# my_person = student('Ronny',23,'Lima-Peru',[15,16,15,6])
# my_person.description()


# 📌 Diseño del Código
# Clase Base: Employee

# Atributos: name (nombre), age (edad), salary (salario base).
# Métodos:
# description(): Muestra la información del empleado.
# Clase Derivada: FullTimeEmployee

# Atributos: hereda de Employee, agrega years_of_service (años de servicio).
# Métodos:
# bonus(): Calcula un bono de acuerdo a los años de servicio. 5 por year
# description(): Llama al método padre y agrega el bono.
# Clase Derivada: PartTimeEmployee

# Atributos: hereda de Employee, agrega hours_worked (horas trabajadas) y hourly_rate (tarifa por hora).
# Métodos:
# calculate_salary(): Calcula el salario basado en horas trabajadas.
# description(): Llama al método padre y agrega el salario calculado.



# class Employee():

#     def __init__(self,name,age,salary):
#         self.name = name 
#         self.age = age
#         self.salary = salary

#     def description(self):
#         print(f'Name:{self.name}\nAge:{self.age}\nSalary:{self.salary}')

# class FullTimeEmployee(Employee):
    
#     def __init__(self, name, age, salary, years_of_service):
#         super().__init__(name, age, salary)

#         self.years_of_service = years_of_service

#     def bonus(self):
        
#         return self.salary * 0.05 * self.years_of_service
    

#     def description(self):
#         super().description()

#         print(f'years of service:{self.years_of_service}\nBono:{self.bonus()}')

# class PartTimeEmployee(Employee):

#     def __init__(self, name, age,hours_worked,hourly_rate):
#         super().__init__(name, age, 0)

#         self.hours_worked = hours_worked
#         self.hourly_rate = hourly_rate
    
#     def calculate_salary(self):

#         return self.hourly_rate * self.hours_worked
    
#     def description(self):
#         super().description() 
#         print(f'Hourly Rate: ${self.hourly_rate:.2f}\nHours Worked: {self.hours_worked}\nTotal Salary: ${self.calculate_salary():.2f}')






# employee_1 = FullTimeEmployee('Ronny',30,5000,5)
# employee_2 = PartTimeEmployee('Juan',22,20,100)
# print('Full-time employee:')
# employee_1.description()
# print('\nPart time employee:')
# employee_2.description()









# Clase Base: Vehicle

# Atributos: brand (marca), model (modelo), year (año de fabricación).
# Métodos:
# description(): Muestra la información del vehículo.
# Clase Derivada: Car

# Atributos: hereda de Vehicle, agrega doors (número de puertas).
# Métodos:
# description(): Llama al método padre y agrega el número de puertas.
# Clase Derivada: Motorcycle

# Atributos: hereda de Vehicle, agrega type_motorcycle (tipo de moto: deportiva, scooter, etc.).
# Métodos:
# description(): Llama al método padre y agrega el tipo de moto.

# class Vehicle():
     
#     def __init__(self,brand, model,year):
          
#           self.brand = brand 
#           self.model = model 
#           self.year = year
          
    
#     def description(self):
#         print(f'Brand:{self.brand}\nModel:{self.model}\nYear:{self.year}')


# class Car(Vehicle):
     
#     def __init__(self, brand, model, year, doors):
#           super().__init__(brand, model, year)

#           self.doors = doors

#     def description(self):
#         super().description()

#         print(f'Number of doors:{self.doors}')


# class Motircycle(Vehicle):
     
#     def __init__(self, brand, model, year,type_motorcycle):
#           super().__init__(brand, model, year)

#           self.type_motorcycle = type_motorcycle

#     def description(self):
#         super().description()
    
#         print(f'Type of motorcycle:{self.type_motorcycle}')

# my_car = Car('Toyota','Yaris',2024,4)
# my_motorcycle = Motircycle('Yamaha','C400',2024,'Choper')


# print('\nDate of car')
# my_car.description()
# print('\nDates of motorcycle')
# my_motorcycle.description()




# Clase Base: ElectronicDevice

# Atributos: brand (marca), model (modelo), price (precio).
# Métodos:
# description(): Muestra la información del dispositivo.
# Clase Derivada: Smartphone

# Atributos: hereda de ElectronicDevice, agrega ram (RAM en GB) y storage (almacenamiento en GB).
# Métodos:
# description(): Llama al método padre y agrega la RAM y el almacenamiento.
# Clase Derivada: Laptop

# Atributos: hereda de ElectronicDevice, agrega processor (procesador) y battery_life (duración de la batería en horas).
# Métodos:
# description(): Llama al método padre y agrega la información adicional.


# class ElectronicDevice():

#     def __init__(self,brand,model,price):
        
#         self.brand = brand
#         self.model = model 
#         self.price = price

#     def description(self):

#         print(f'Brand:{self.brand}\nModel:{self.model}\nPrice:{self.price}')


# class Smarphone(ElectronicDevice):
    
#     def __init__(self, brand, model, price,ram,storage):
#         super().__init__(brand, model, price)

#         self.ram = ram 
#         self.storage = storage

#     def description(self):
#         super().description()

#         print(f'Ram:{self.ram}GB\nstorage:{self.storage}GB')

    
# class Laptop(ElectronicDevice):

#     def __init__(self, brand, model, price, processor, battery_life):
#         super().__init__(brand, model, price)

#         self.processor = processor
#         self.battery_life = battery_life


#     def description(self):
#         super().description()

#         print(f'Processor:{self.processor}\nBattery life:{self.battery_life}%')

# print('\nDate of Smarphone')
# my_smarphone = Smarphone('samsung','S21',2000,12,128)
# my_smarphone.description()
# print('\nDate of Laptop')
# my_laptop = Laptop('Asus','VivoBook',1799,'Core i5',80)
# my_laptop.description()








