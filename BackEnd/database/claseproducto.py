    # Clase Productos

class Producto:
    def __init__ (self,nombre_producto,descripcion_producto,imagen_producto,precio_producto,id_producto=0,id_tienda=0):
        self.nombre_producto = nombre_producto
        self.descripcion_producto = descripcion_producto
        self.imagen_producto = imagen_producto
        self.precio_producto = precio_producto
        self.id_producto = id_producto
        self.id_tienda =id_tienda
            
    # Editar Productos
    def editar_nombre_producto (self,nuevo_nombre_producto):
        self.nombre_producto = nuevo_nombre_producto
        return("Se ha modificado el nombrel producto ha",nuevo_nombre_producto)

    def editar_descripcion_producto (self,nueva_descripcion_producto):
        self.descripcion_producto = nueva_descripcion_producto
        return("Se ha modificado la descripcion del producto ha",nueva_descripcion_producto)
    
    def editar_imagen_producto (self,nueva_imagen_producto):
        self.imagen_producto = nueva_imagen_producto
        return("Se ha modificado la imagen del producto")

    def editar_precio_producto (self,nueva_precio_producto):
        self.precio_producto = nueva_precio_producto
        return("Se ha modificado el precio del producto a $ ",nueva_precio_producto)

    # Borrar Producto
    def __del__(self):
        return("Se ha borrado el producto",self.id_producto)
    
    # Mostrar datos el producto
    def __str__(self):
        return("EL producto {} con la descripcion {} tiene el precio {}".format(self.nombre_producto,self.descripcion_producto,self.precio_producto)) 

