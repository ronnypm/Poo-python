class Producto():
    def __init__(self,id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    
    def __str__(self):
        return f'{self.nombre} (ID: {self.id}, Precio: {self.precio}, Cantidad: {self.cantidad})'



class Inventario:
    def __init__(self):
        self.productos = {}

    
    def agregar_producto(self,producto):
        if producto.id in self.productos:
            print('El producto ya existe. Actualizando cantidad.')
            self.productos[producto.id].cantidad += producto.cantidad
        else:
            self.productos[producto.id] = producto



inventari_1 = Inventario()
producto_1 = Producto(1,'manzana', 0.50, 100)
print(inventari_1.productos)
inventari_1.agregar_producto(producto_1)
print(inventari_1.productos)