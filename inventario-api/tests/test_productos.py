from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from database import Base, get_db

# Base de datos en memoria solo para tests
SQLALCHEMY_TEST_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_TEST_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "mensaje" in response.json()

def test_crear_producto():
    response = client.post("/productos/", json={
        "nombre": "Laptop",
        "descripcion": "Laptop gamer",
        "precio": 1500.00,
        "stock": 10
    })
    assert response.status_code == 201
    data = response.json()
    assert data["nombre"] == "Laptop"
    assert data["precio"] == 1500.00

def test_get_productos():
    response = client.get("/productos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_producto_por_id():
    # Primero creamos uno
    crear = client.post("/productos/", json={
        "nombre": "Monitor",
        "precio": 300.00,
        "stock": 5
    })
    producto_id = crear.json()["id"]

    response = client.get(f"/productos/{producto_id}")
    assert response.status_code == 200
    assert response.json()["id"] == producto_id

def test_get_producto_no_existe():
    response = client.get("/productos/9999")
    assert response.status_code == 404

def test_actualizar_producto():
    crear = client.post("/productos/", json={
        "nombre": "Teclado",
        "precio": 50.00,
        "stock": 20
    })
    producto_id = crear.json()["id"]

    response = client.put(f"/productos/{producto_id}", json={"precio": 45.00})
    assert response.status_code == 200
    assert response.json()["precio"] == 45.00

def test_eliminar_producto():
    crear = client.post("/productos/", json={
        "nombre": "Mouse",
        "precio": 25.00,
        "stock": 15
    })
    producto_id = crear.json()["id"]

    response = client.delete(f"/productos/{producto_id}")
    assert response.status_code == 204

    # Verificar que ya no aparece en el listado
    get = client.get(f"/productos/{producto_id}")
    assert get.json()["activo"] == False