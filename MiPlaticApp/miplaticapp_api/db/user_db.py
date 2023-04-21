from sqlalchemy import Column, Integer, String
from db.db_conection import Base, engine

class UserInDB(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True, unique=True)
    password = Column(String)
    balance  = Column(Integer)

#Funcion para poder realizar consulta sql alchemy, para cuando se imprima usuario de a conocer la informacion en string
    def __str__(self):
        return "Cliente: " + str(self.username) + ", Clave: " + str(self.password) + ", Saldo dinero: " + str(self.balance)

#se cree las tablas en postgres
Base.metadata.create_all(bind=engine)

#Se crea la entidad de datos y con la ultima línea se hace el proceso de creación de la tabla.