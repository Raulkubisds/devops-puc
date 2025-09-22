"""Testes automatizados para o módulo main."""

from main import read_root


def test_passando():
    """Teste que sempre passa."""
    assert True

def test_read_root():
    """Teste da função read_root()."""
    response = read_root()
    assert response == {"hello": "world"}

# tests/test_app.py

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_message():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "API funcionando no Docker!"}

def test_soma_positiva():
    response = client.get("/soma/2/3")
    assert response.status_code == 200
    assert "resultado" in response.json()
    assert response.json() == {"resultado": 5}

def test_soma_zero():
    response = client.get("/soma/0/5")
    assert response.status_code == 200
    assert response.json()["resultado"] == 5

def test_soma_negativa():
    response = client.get("/soma/-2/-3")
    assert response.status_code == 200
    assert response.json()["resultado"] == -5

def test_soma_valores_mistos():
    response = client.get("/soma/-2/3")
    assert response.status_code == 200
    assert response.json()["resultado"] == 1
