# Clase Tienda
class Tienda:
    # Construir tienda
    def __init__ (self,nombre_tienda,direccion_tienda,categoria,imagen_portada_tienda,contacto,id_tienda=0):
        self.nombre_tienda = nombre_tienda
        self.direccion_tienda = direccion_tienda
        self.categoria = categoria
        self.imagen_portada_tienda = imagen_portada_tienda
        self.contacto = contacto
        self.id_tienda = id_tienda
        
        
    # Editar datos de la tienda
    def editar_nombre (self,nuevo_nombre):
        self.nombre_tienda = nuevo_nombre
        print("Se ha modificado el nombre de la tienda ha",nuevo_nombre)

    def editar_direccion_tienda (self,nueva_direccion_tienda):
        self.direccion_tienda = nueva_direccion_tienda
        print("Se ha modificado la direcion de tienda ha",nueva_direccion_tienda)
    
    def editar_categoria (self,nueva_categoria):
        self.categoria = nueva_categoria
        print("Se ha modificado la categoria por",nueva_categoria)

    def editar_imagen_portada_tienda (self,nueva_imagen_portada_tienda):
        self.imagen_portada_tienda = nueva_imagen_portada_tienda
        print("Se ha modificado la imagen de portada")


    # Borrar Tienda
    def __del__(self):
        print("Se ha borrando la Tienda",self.id_tienda)
    
    # Mostrar datos de la tienda
    def __str__(self):
        return("La tienda {} ubicada en {} de la categoria {} la puedes contactar atraves de {}".format(self.nombre_tienda,self.direccion_tienda,self.categoria,self.contacto)) 

