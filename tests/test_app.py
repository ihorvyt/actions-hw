from myapp.app import add, subtract

def test_get_add():
    result = add(2,2);
    assert result == 4;

def test_get_subtract():
    result = subtract(4,2);
    assert result == 2;