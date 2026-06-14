from fastapi import FastAPI
from app.routers import graphql_router
from fastapi.middleware.cors import CORSMiddleware

from app.database.connection import engine, Base
from app.models.stock import StockActual

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de GraphQL",
    root_path="/graphql",  
    docs_url="/docs",          
    openapi_url="/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(graphql_router.router, prefix="")

@app.get("/", tags=["Raíz"])
def leer_raiz():
    return {
        "status": "Online",
        "servicio": "GraphQL (graphql-api)",
        "mensaje": "Servidor listo. Navega a /graphql para abrir el entorno de pruebas interactivo"
    }