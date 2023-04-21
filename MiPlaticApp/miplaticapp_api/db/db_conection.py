#identifica el motor de BD a utilizar
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
#enlazar la capa logica con la BD
from sqlalchemy.orm import sessionmaker

#creación del motor de BD postgres
#Los valores de DATABASE_URL deben ser remplazados por los correspondientes.
#DATABASE_URL = "postgresql://user:password@host:port/name_db"
CONEXION_A_BD = "postgresql://postgres:root@localhost:5432/miplaticaap" 
engine 		  = create_engine(CONEXION_A_BD)

#Establecer una sesión con la BD, y crear la funcionalidad para inyectar las dependencias.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#get_db será la encargada de inyectar la dependencia, es decir, SessionLocal().
def get_db():
	db = SessionLocal()
	try:
		yield db	#Mantiene la sesion
	finally:
		db.close()

#Crear el modelo que se usará como base para la creación de las entidades de datos.
#Base permitirá definir entidades de datos a partir de ella, estas entidades se convertirán en tablas.
Base = declarative_base()
Base.metadata.schema = "cajadb"