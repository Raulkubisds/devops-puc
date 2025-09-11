# test_main.py

from main import read_root

def test_passando():
    assert True

def test_read_root():
    response = read_root()
    assert response == {"hello": "world"}