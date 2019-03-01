import sqlite3

class Database():
	"""Permite conectar a base de datos, insertar, consultar, modificar y borrar registros.
	
	No recibe parámetros inicialmente, 
	Métodos principales: guardar(object),modificar(id,columna,new_data),borrar(id),extraer(id),all_tiendas().
	
	Database.guardar(object) recibe un objeto de la clase Tienda como parámetro y guarda sus datos en la db si es que 
	el nombre no se repite. 
	Database.modificar(id,columna,new_data) recibe el id de la tienda a modificar, el nombre de la columna (nombre, 
	direccion, categoria,ruta_imagen o contacto) cambia el dato que esta en la tabla por new_data.
	Database.borrar(id) recibe el id de la tienda y borra su contenido en la base de datos.
	Database.extraer(id) recibe el id de la tienda almacenada en la base de datos y devuelve un objeto de la clase 
	Tienda con esos datos.
	Database.all_tiendas() devuelve una lista de tuplas que contiene cada una los datos de todas las tiendas almacenadas 
	en la base de datos.
	Estos métodos tambíen se encargan de crear la tabla si es necesario, como tambíen de establecer conexión con el 
	archivo, abrir el cursor, realizar el commit, cerrar el cursor y cerrar la conexión a través de los métodos 
	necesarios."""
	
	def __init__(self):
		"""Método inicializador, no recibe parámetros inicialmente"""
		
				
	def conect(self):
		"""Establece conexión con el archivo por defecto database.db"""
		
		self.db=sqlite3.connect("database.db")
		self.cursor =self.db.cursor()
		

	def crear_tabla(self):
		"""Crea la tabla "tiendas" si no existe, con cinco columnas """
		
		return self.cursor.execute('''CREATE TABLE IF NOT EXISTS tiendas (
									   id INTEGER PRIMARY KEY AUTOINCREMENT,
									   nombre TEXT NOT NULL UNIQUE,
									   direccion TEXT NOT NULL ,
									   categoria TEXT NOT NULL,
									   ruta_imagen TEXT NOT NULL,
									   contacto TEXT NOT NULL)''')
		
	def datos(self):
		"""Para poder trabajar con los datos de objetos de clase Tienda
		agrega los datos extraídos del objeto a la lista interna params[] """
	
		self.params.append(self.nombre)
		self.params.append(self.direccion)
		self.params.append(self.categoria)
		self.params.append(self.ruta_imagen)
		self.params.append(self.contacto)
		
	def guardar(self,object,params=[]):
		"""Recibe un objeto de la clase Tienda y permite insertar sus datos en la tabla tiendas,
		para esto crea la lista params, en la cual a través del método datos() se introducen los datos de la tienda,
		para luego enviarlos a la sentencia que inserta los datos.
		Luego deja vacía la lista params."""
		params= []
		self.params=params
		self.nombre=object.nombre_tienda 
		self.direccion=object.direccion_tienda 
		self.categoria=object.categoria 
		self.ruta_imagen= object.imagen_portada_tienda
		self.contacto = object.contacto
		self.datos()
		try:
			self.conect()
			self.crear_tabla()
			self.cursor.execute("INSERT INTO tiendas(nombre,direccion,categoria,ruta_imagen,contacto) VALUES (?,?,?,?,?);",self.params)
			self.params.clear()
			self.commit()
			self.cerrar()
		except sqlite3.IntegrityError as error:
			return "error posiblemente hay un dato con el mismo nombre"
			
		self.params.clear()
		
		
	def modificar (self,id,columna,new_data):
		"""Modifica los datos almacenados en la db, correspondientes al id de la tienda,
		necesariamente se deben pasar los tres parámetros requeridos,id de la tienda, nombre de 
		la columna a modificar y el dato nuevo."""
		
		try:
			self.conect()
			self.cursor.execute("UPDATE tiendas SET {} = ? WHERE id = ?;".format(columna),(new_data,id))
			self.commit()
			self.cerrar()
		except sqlite3.IntegrityError as error:
			return(error)
			
	def borrar(self, id):
		"""Borra los datos almacenados en la db, correspondientes al id de la tienda, 
		necesariamente se debe pasar el parámetro requerido id de la tienda a borrar"""
		
		try:
			self.conect()
			self.cursor.execute("DELETE FROM tiendas WHERE id = ?;",[id])
			self.commit()
			self.cerrar()
		except sqlite3.IntegrityError as error:
			return(error)

	def commit(self):
		"""El método commit valida las transacciones 
		realizadas en la base de datos, se ejecuta luego de realizar transacciones que 
		modifiquen la base de datos"""
		
		self.db.commit()
		
		
	def cerrar(self):
		"""Cierra el cursor y la conexión a la base de datos"""
		
		self.cursor.close()
		self.db.close()

	def extraer(self,id):
		"""Extrae los datos de la tabla referentes al parámetro id, el cual debe recibir necesariamente,
		retorna un objeto de clase Tienda generado a partir de los datos obtenidos 
		desde la base de datos, se puede almacenar en una variable que se debe asignar en la declaración 
		Ej: tienda_recuperada=Database.extraer(id)"""
		
		self.conect()
		self.cursor.execute("SELECT * FROM tiendas WHERE id = ?;",[id])
		tienda = self.cursor.fetchall()
		self.cerrar()
		data=tienda[0]
		tienda_rec = Tienda(data[1],data[2],data[3],data[4],data[5])
		return tienda_rec
		
	def all_tiendas(self):
		"""devuelve una lista con los datos de todas la tiendas, separados en tuplas"""
		
		self.conect()
		self.cursor.execute("SELECT * FROM tiendas")
		tiendas = self.cursor.fetchall()
		self.cerrar()
		lista=[]
		for registro in tiendas:
			lista.append(registro)
		return lista
		
	def __str__(self):
		"""string del objeto"""
		
		return ("Objeto de clase Database")
	 
	def __del__(self):
		"""Elimina el objeto """
