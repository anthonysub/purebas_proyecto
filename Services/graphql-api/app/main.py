from fastapi import FastAPI
from routers import graphql_router
from fastapi.middleware.cors import CORSMiddleware
from database.connection import engine, Base
from models.stock import StockActual

# Crear tablas al iniciar
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de GraphQL",
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

# Montamos el router de GraphQL directamente en /graphql
# Así Traefik (que envía /graphql) coincidirá exactamente.
app.include_router(graphql_router.router, prefix="/graphql")

@app.get("/", tags=["Raíz"])
def leer_raiz():
    return {
        "status": "Online",
        "servicio": "GraphQL (graphql-api)",
        "mensaje": "Servidor listo. Navega a /graphql para abrir el entorno de pruebas interactivo"
    }
