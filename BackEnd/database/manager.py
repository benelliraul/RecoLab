from clasetienda import Tienda
from claseproducto import Producto
from db_tiendas import Db_tiendas
from db_productos import Db_productos

class Manager(Db_tiendas,Db_productos):
    """Clase Manager hereda de las clases Db_tiendas y Db_productos,
    Facilita el manejo de la base de datos acediendo a los metodos necesarios para
    guardar, modificar, consultar y borrar, tanto Tiendas como Productos.
    Para agregar Tiendas recibe un objeto Tienda y guadra la info en la tabla.
    Para agregar Productos recibe un objeto Producto y un objeto Tienda al cual se vincula.
    Para las consultas, si la consulta admite varios resultados siempre devuelve una lista de 
    objetos(Tienda o Producto), si la consulta no obtiene datos de las tablas devuelve una
    lsita con un objeto (Tienda o Producto) con los campos por defecto 'nulo'.
    Si la consulta admite un solo resultado devuelve un objeto(Tienda o Producto), si la
    consulta no obtine datos de las tablas devuelve un objeto (Tienda o Producto) con los
    campos por defecto:'nulo'.
    Metodos :
        agregar_tienda(self, tienda)
        modificar_datos_tienda(self, id_tienda, nombre_columna, datos_nuevos)
        extraer_tienda(self, id_tienda)
        extraer_n_tiendas_orden(self,n=10,contiene ='',orden='desc',columna=
                                'nombre||direccion||categoria||contacto')
        extraer_todas_tiendas(self)
        borrar_tienda(self, id_tienda)

        agregar_producto(self,producto,tienda)
        modificar_datos_producto(self, id_producto, nombre_columna, datos_nuevos)
        extraer_productos_tienda(self,id_tienda='')
        extraer_productos_coinciden(self,n=10,contiene ='',columna=
                                'nombre||descripcion||precio',orden='desc')
        borrar_producto(self,id_producto,id_tienda)



    """
    pass
       