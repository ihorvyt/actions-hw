from myapp.app import add, subtract

def test_add():
    assert add(2,3) == 5

def test_subtract():
    assert subtract(4,2) == 2