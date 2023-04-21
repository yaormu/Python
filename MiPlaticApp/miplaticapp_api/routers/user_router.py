from typing import List
from fastapi import Depends, APIRouter, HTTPException

from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, text, func

from db.db_conection import get_db
from db.user_db import UserInDB
from db.transaction_db import TransactionInDB

from models.user_models import UserIn, UserOut
from models.transaction_models import TransactionIn, TransactionOut

router = APIRouter()

@router.post("/user/auth/")
async def auth_user(user_in: UserIn, db: Session = Depends(get_db)):
    
    user_in_db = db.query(UserInDB).get(user_in.username)
    
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if user_in_db.password != user_in.password:
        raise HTTPException(status_code=403, detail="Error de autenticacion")

    return {"Autenticado": True}


@router.get("/user/balance/{username}", response_model=UserOut)
async def get_balance(username: str, db: Session = Depends(get_db)):
    
    user_in_db = db.query(UserInDB).get(username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    
    return user_in_db

#Prueba con instrucciones SQL Alchemy
#@router.get("/examples")
#async def examples(db: Session = Depends(get_db)):
    #Ingresar usuario a la BD postgres
    '''
    user1 = UserInDB(username = "Paco", password="paco", balance=1000000)
    db.add(user1)
    db.commit()
    '''
    #Ingresar varios usuarios a la BD postgres
    '''
    user1 = UserInDB(username = "Herib", password = "herib", balance = 1000000)
    user2 = UserInDB(username = "Tavo", password = "tavo", balance = 1000000)
    db.add_all([user1, user2])
    db.commit()
    '''
    #Mostrar usuario registrados ordenadamente por nombre
    '''
    users = db.query(UserInDB).order_by(UserInDB.username)
    
    for usuarios in users:
        print(usuarios.username, usuarios.password, usuarios.balance)
    '''
    #Mostrar solo usuario y balance
    '''
    users = db.query(UserInDB.username, UserInDB.balance)
    
    for usuarios in users:
        print(usuarios.username, usuarios.balance)
    '''
    #Representacion string consulta usuarios
    '''
    users = db.query(UserInDB, UserInDB.username)
    
    for usuarios in users:
        print(usuarios.UserInDB, usuarios.username)
    '''
    #consulta usuarios mostrar los dos primeros
    '''
    users = db.query(UserInDB.username.label('usuario'))
    
    for usuarios in users[0:2]:
        print(usuarios.usuario)
    '''
    #filtro usuario especifico o lo que querramos
    '''
    users = db.query(UserInDB).filter(UserInDB.username == "Tavo")
    
    for usuarios in users:
        print(usuarios)
    '''
    #filtro usuario que cumpla con el user y password
    '''
    users = db.query(UserInDB).\
            filter(UserInDB.username == "Tavo").\
            filter(UserInDB.password == "tavo")
    
    for usuarios in users:
        print(usuarios)
    '''
    #filtro usuario que empieza con he
    '''
    users = db.query(UserInDB).\
            filter(UserInDB.username.like('He%'))
    
    for usuarios in users:
        print(usuarios)
    '''
    #filtro usuario que tenga la letra a
    #en caso no tener en cuenta May o Min ilike
    '''
    users = db.query(UserInDB).\
            filter(UserInDB.username.like('%a%'))
    
    for usuarios in users:
        print(usuarios)
    '''
    #Traer usuario que no esten en esta lista
    '''
    users = db.query(UserInDB).\
            filter(UserInDB.username.notion(["Lucy", "Rigo", "Erika", "Heri", "Tavo"]))
    
    for usuarios in users:
        print(usuarios)
    '''
    #No se recomienda realizar estas consulta sql desde aqui, por seguridad en inyeccion de dependencia
    '''
    users = db.query(UserInDB).\
        from_statement(text("SELECT * FROM cajadb.users WHERE username LIKE :username")).\
        params(username='Tavo')
    
    users_list = users.one_or_none()
    print(users_list)
    print("***********")
    
    for u in users.all():
        print(u)
    '''
    #Nos indica en postman si fue realizada la consulta  
    #return {"Message": "Consulta correctamente"}
#code work in local
#@router.get("/examples")
#async def example(db: Session = Depends(get_db)):
    
   #agregar usuario a la bd
    #user1 = UserInDB(username = "camilo77", password = "123456", balance = 100000)
    #db.add(user1)
    #db.commit()

    #agregar varios usuarios a la bd
    #user1 = UserInDB(username = "juan25", password = "hola", balance = 120000)
    #user2 = UserInDB(username = "andres15", password = "password", balance = 80000)
    #db.add_all([user1, user2])
    #db.commit()
    

    #consulta e iteracion
    #users = db.query(UserInDB).order_by(UserInDB.username)

    #for u in users:
    #    print(u.username, u.password, u.balance)

    #return {"Message" : "Todo funciona Bien"}
    #db.refresh(user1)

    #user_in_db = db.query(UserInDB).get(user_in.username)