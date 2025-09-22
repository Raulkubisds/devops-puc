
def test_passando():
    assert True

def test_read_root():
    response = read_root()
    assert response == {"hello": "world"}

def read_root():
    return {"hello": "world"}