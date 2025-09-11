from  main import read_root

def test_passando():
    assert True

def test_read_root ():
    responses = read_root()
    assert responses == {"hello": "world"}