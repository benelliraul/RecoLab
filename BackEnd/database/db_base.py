import sqlite3

class Basedatos:
    """Contiene los metodos basicos para interactuar con la base de datos."""

    def __init__(self):
       
        self.crear_tabla()

    def conectar_base_datos(self):
        
        self.db = sqlite3.connect("base_datos.db")
        self.cursor = self.db.cursor()

    def commit(self):
        
        self.db.commit()

    def cerrar_conexion(self):
       
        self.cursor.close()
        self.db.close()

    def crear_tabla(self):
        """Crea las tablas "tiendas" y "productos" si no existen, agrega claves primarias a
        cada registro """

        tablas=['''CREATE TABLE IF NOT EXISTS tiendas (
									   id_tienda INTEGER PRIMARY KEY AUTOINCREMENT,
									   nombre TEXT NOT NULL UNIQUE,
									   direccion TEXT NOT NULL ,
									   categoria TEXT NOT NULL,
									   ruta_imagen TEXT NOT NULL,
									   contacto TEXT NOT NULL)''',
                                       
                                       '''CREATE TABLE IF NOT EXISTS productos (
									   id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
                                       nombre TEXT NOT NULL ,
									   descripcion TEXT NOT NULL ,
									   ruta_imagen TEXT NOT NULL,
									   precio TEXT NOT NULL,
									   id_tienda_madre INTEGER,
                                       CONSTRAINT prod_unico UNIQUE(
                                           nombre,descripcion,ruta_imagen,
                                           id_tienda_madre
                                       )
                                       FOREIGN KEY (id_tienda_madre) REFERENCES tiendas(id_tienda));''']
        self.conectar_base_datos()
        for tabla in tablas:
            self.cursor.execute(tabla)
        
