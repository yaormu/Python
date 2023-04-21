from fastapi import Depends, FastAPI

from fastapi.middleware.cors import CORSMiddleware

#selecionamos el router dentro del archivo y lo renombramos
from routers.user_router import router as router_users
from routers.transaction_router import router as router_transactions

api = FastAPI()

#Se registran los router, para mi que mi aplicacion api va utilizar los servicios definidos
api.include_router(router_users)
api.include_router(router_transactions)

#CORS para que funcionen nuestras vistas
origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost/8000", "http://localhost/8080",
    "http://127.0.0.1:8000", "http://127.0.0.1:8080", 
    "http://127.0.0.1:8000/user/auth/",
    "https://frontend-miplaticapp.herokuapp.com"
]

api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)