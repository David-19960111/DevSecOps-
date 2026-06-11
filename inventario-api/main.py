from fastapi import FastAPI
from database import engine
import models
from routers import productos

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Inventario API",
    description="API REST para gestión de productos",
    version="1.0.0"
)

app.include_router(productos.router)

@app.get("/")
def root():
    return {"mensaje": "Bienvenido a la API de Inventario"}