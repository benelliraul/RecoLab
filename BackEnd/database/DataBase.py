import sqlite3
from tienda import Tienda


class Basedatos:
    """Permite conectar a base de datos, insertar, consultar, modificar y borrar registros."""

    def __init__(self):
        """Crea la tabla "tiendas" solo si no existe """

        self.crear_tabla()

    def conectar_base_datos(self):
        """Establece conexión con el archivo "base_datos.db", crea el objeto cursor."""

        self.db = sqlite3.connect("base_datos.db")
        self.cursor = self.db.cursor()

    def commit(self):
        """Valida las transacciones realizadas en la base de datos, se ejecuta
        luego de realizar transacciones que modifiquen la base de datos"""

        self.db.commit()

    def cerrar_conexion(self):
        """Cierra el cursor y la conexión a la base de datos"""

        self.cursor.close()
        self.db.close()

    def crear_tabla(self):
        """Crea la tabla "tiendas" si no existe, con seis  columnas, la primera
        reservada para clave primaria que se añade automaticamete, no admite dos
        registros iguales para la columna "nombre" """

        self.conectar_base_datos()
        return self.cursor.execute('''CREATE TABLE IF NOT EXISTS tiendas (
									   id INTEGER PRIMARY KEY AUTOINCREMENT,
									   nombre TEXT NOT NULL UNIQUE,
									   direccion TEXT NOT NULL ,
									   categoria TEXT NOT NULL,
									   ruta_imagen TEXT NOT NULL,
									   contacto TEXT NOT NULL)''')

    def guardar_tienda(self, tienda):
        """Recibe un objeto de la clase Tienda y permite insertar sus datos en la 
        tabla tiendas."""

        datos_tienda = [tienda.nombre_tienda, tienda.direccion_tienda,
						tienda.categoria, tienda.imagen_portada_tienda,tienda.contacto]
        try:
            self.conectar_base_datos()
            self.cursor.execute('''INSERT INTO tiendas(
									nombre,direccion,categoria,
									ruta_imagen,contacto) VALUES 
									(?,?,?,?,?);''', datos_tienda)
            self.commit()
            self.cerrar_conexion()
            return True
        except sqlite3.IntegrityError as error:
            return error 

    def modificar_datos_tienda(self, id_tienda, nombre_columna, datos_nuevos):
        """Modifica los datos almacenados en la base de datos, correspondientes 
        al id de la tienda, necesariamente se deben pasar los tres parámetros 
        requeridos, id de la tienda, nombre de la columna a modificar y el dato nuevo."""

        try:
            self.conectar_base_datos()
            self.cursor.execute("UPDATE tiendas SET {} = ? WHERE id = ?;"
								.format(nombre_columna), (datos_nuevos, id_tienda))
            self.commit()
            self.cerrar_conexion()
            return True
        except sqlite3.IntegrityError as error:
            return (error)

    def devolver_lista_objetos(self,tiendas):
        """Toma una lista con los resultados de una consulta a
        la tabla tiendas y devuelve una lista de objetos Tienda"""

        lista_tiendas = []
        for registro in tiendas:
                objeto=Tienda(registro[1],registro[2],registro[3],
                            registro[4],registro[5])
                lista_tiendas.append(objeto)
        return(lista_tiendas)

    def extraer_tienda(self, id_tienda): #se podria hacer con el nombre
        """Extrae los datos de la tabla referentes al parámetro id.
        
        El cual debe recibir necesariamente, retorna un objeto de clase Tienda 
        generado a partir de los datos obtenidos, se puede almacenar en una variable 
        que se debe asignar en la declaración
        Ej: tienda_recuperada=Basedatos.extraer_tienda(id)"""

        self.conectar_base_datos()
        self.cursor.execute("SELECT * FROM tiendas WHERE id = ?;", id_tienda)
        tienda = self.cursor.fetchone()
        self.cerrar_conexion()
        lista_datos = tienda[0]
        tienda_extraida = Tienda(lista_datos[1], lista_datos[2], lista_datos[3],
                                lista_datos[4], lista_datos[5])
        return tienda_extraida
    
    def extraer_n_tiendas_orden(self,n=10,contiene ='',orden='DESC',columna=
                                'nombre||direccion||categoria||contacto'):
        """Devuelve 10 ultimas tiendas, puede buscar coincidencia en columnas y variar el orden.

        Acepta parametros: n, orden, contiene y columna.El parametro n debe ser un
        numero entero, orden puede ser 'DESC' (descendente),'ASC'(ascendente) o 
        'aleatorio', devuelve una lista de n Tiendas ordenada segun el parametro 'orden' 
        pudiendo filtrar resultados especificando el contenido a buscar en 'contiene' 
        y el nombre de la 'columna', por defecto buscara en todas las columnas
        """

        self.conectar_base_datos()
        if orden == "aleatorio":
            self.cursor.execute("SELECT * FROM tiendas WHERE {} LIKE '%{}%' ORDER BY random() LIMIT ?;".format(columna,contiene),[n])
        else:
            self.cursor.execute("SELECT * FROM tiendas WHERE {} LIKE '%{}%' ORDER BY id {} LIMIT ?;".format(columna,contiene,orden),[n])    
        tiendas = self.cursor.fetchall()
        self.cerrar_conexion()
        return self.devolver_lista_objetos(tiendas)
		
    def extraer_todas_tiendas(self):
        """Devuelve una lista de objetos de todas las tiendas almacenadas en la base 
        de datos"""

        self.conectar_base_datos()
        self.cursor.execute("SELECT * FROM tiendas")
        tiendas = self.cursor.fetchall()
        self.cerrar_conexion()
        return self.devolver_lista_objetos(tiendas)  

    def borrar_tienda(self, id_tienda):
        """Borra los datos almacenados en la base de datos, correspondientes al id de 
        la tienda, necesariamente se debe pasar el parámetro requerido id de la tienda
        a borrar"""

        try:
            self.conectar_base_datos()
            self.cursor.execute("DELETE FROM tiendas WHERE id = ?;", [id_tienda])
            self.commit()
            self.cerrar_conexion()
            return True
        except sqlite3.IntegrityError as error:
            return (error)

    def __str__(self):
        """Objeto de clase Basedatos"""

    def __del__(self):
        """Elimina el objeto """
