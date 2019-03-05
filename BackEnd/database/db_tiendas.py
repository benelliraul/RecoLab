import sqlite3
from db_base import Basedatos
from clasetienda import Tienda


class Db_tiendas(Basedatos):
    """Permite interactuar con la talba tiedas"""

    def agregar_tienda(self, tienda):
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
        except sqlite3.IntegrityError :
            return False

    def modificar_datos_tienda(self, id_tienda, nombre_columna, datos_nuevos):
        """Modifica los datos almacenados en la base de datos, correspondientes 
        al id de la tienda, necesariamente se deben pasar los tres parámetros 
        requeridos, id de la tienda, nombre de la columna a modificar y el dato nuevo."""

        try:
            self.conectar_base_datos()
            self.cursor.execute("UPDATE tiendas SET {} = ? WHERE id_tienda = ?;"
								.format(nombre_columna), [datos_nuevos, id_tienda])
            self.commit()
            self.cerrar_conexion()
            return 
        except sqlite3.OperationalError:
            return False

    def devolver_lista_tiendas(self,tiendas):
        """Se utiliza internamente, toma una lista con los resultados de una consulta a
        la tabla tiendas y devuelve una lista de objetos Tienda"""

        lista_tiendas = []
        for registro in tiendas:
                objeto=Tienda(registro[1],registro[2],registro[3],
                            registro[4],registro[5])
                lista_tiendas.append(objeto)
        return(lista_tiendas)

    def no_hay_coincidencias(self):
        """Se utiliza internamente, genera un objeto Tienda con datos por defecto 
        para devolver en consultas que no arrojen resultados"""

        return(Tienda('nulo','nulo','nulo','nulo','nulo'))

    def extraer_tienda(self, id_tienda=0): 
        """Extrae los datos de la tabla tiendas referentes al parámetro id.
        
        El cual debe recibir necesariamente, retorna un objeto de clase Tienda 
        generado a partir de los datos obtenidos, se puede almacenar en una variable 
        que se debe asignar en la declaración
        Ej: tienda_recuperada=Basedatos.extraer_tienda(id)
        Si la busqueda no obtiene resultados devuelve un objeto por Tienda por defecto 
        """

        self.conectar_base_datos()
        self.cursor.execute("SELECT * FROM tiendas WHERE id_tienda = ?;", [id_tienda])
        tienda = self.cursor.fetchone()
        self.cerrar_conexion()

        if str(tienda)== 'None': #verifica que la consulta devuelva algun dato
            return self.no_hay_coincidencias() #objeto con datos por defecto
        else:
            tienda_extraida = Tienda(tienda[1], tienda[2], tienda[3],tienda[4], tienda[5],tienda[0])
            return tienda_extraida
        
    def extraer_n_tiendas_orden(self,n=10,contiene ='',orden='desc',columna=
                                'nombre||direccion||categoria||contacto'):
        """Devuelve 10 ultimas tiendas, puede buscar coincidencia en columnas y variar el orden.
        Acepta parametros: n, orden, contiene y columna.El parametro n debe ser un
        numero entero representa la cantidad maxima de objetos a devolver, orden puede ser
        'desc' (descendente),'asc'(ascendente) o 'aleatorio'; 'contiene' representa
        el contenido que se desea buscar y 'columna' el nombre de la columna en la tabla.
        Devuelve una lista de Tiendas ordenada segun el parametro 'orden'. 
        """

        if columna !='nombre' and columna != 'direccion' and columna !='categoria' and columna != 'contacto':
            columna='nombre||direccion||categoria||contacto' 
        self.conectar_base_datos()
        if orden != 'desc' and orden != 'asc' and orden !='aleatorio':
            orden='desc'
        if orden == "aleatorio":
            self.cursor.execute("SELECT * FROM tiendas WHERE {} LIKE '%{}%' ORDER BY random() LIMIT ?;".format(columna,contiene),[n])
        else:
            self.cursor.execute("SELECT * FROM tiendas WHERE {} LIKE '%{}%' ORDER BY id_tienda {} LIMIT ?;".format(columna,contiene,orden),[n])    
        tiendas = self.cursor.fetchall()
        self.cerrar_conexion()
        if len(tiendas)==0:
            return [self.no_hay_coincidencias()]#devuelde el objeto en una lista porque supuse que es lo que se espera recibir,aunque solo tiene un objeto vacio
        else:
            return self.devolver_lista_tiendas(tiendas)
		
    def extraer_todas_tiendas(self):
        """Devuelve una lista de objetos de todas las tiendas almacenadas en la base 
        de datos"""

        self.conectar_base_datos()
        self.cursor.execute("SELECT * FROM tiendas")
        tiendas = self.cursor.fetchall()
        self.cerrar_conexion()
        
        if len(tiendas)==0:
            return [self.no_hay_coincidencias()]
        else:
            return self.devolver_lista_tiendas(tiendas)
          
    def borrar_tienda(self, id_tienda):
        """Borra los datos almacenados en la base de datos, correspondientes al id de 
        la tienda, necesariamente se debe pasar el parámetro requerido id de la tienda
        a borrar"""

        try:
            self.conectar_base_datos()
            self.cursor.execute("DELET FROM productos WHERE id_tienda madre = ?",[id_tienda])
            self.cursor.execute("DELETE FROM tiendas WHERE id_tienda = ?;", [id_tienda])
            self.commit()
            self.cerrar_conexion()
        except sqlite3.IntegrityError:
            return False
            
    