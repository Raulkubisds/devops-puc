"""Testes automatizados para o módulo main."""

from main import read_root


def test_passando():
    """Teste que sempre passa."""
    assert True

def test_read_root():
    """Teste da função read_root()."""
    response = read_root()
    assert response == {"hello": "world"}
