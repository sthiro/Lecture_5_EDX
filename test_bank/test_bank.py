from bank import value
import pytest

def test_default():

    assert value("hello") == 0
    assert value("hi") == 20
    assert value("welcome") == 100
    assert value("what's happening") == 100

def test_Case():

    assert value("HELLO") == 0
    assert value("hEllo") == 0

    assert value("Hi") == 20
    assert value("HI") == 20

    assert value("Welcome") == 100
    assert value("WELCOME") == 100

def test_punctuation():

    assert value("hello!") == 0
    assert value("hi!") == 20
    assert value("welcome!") == 100
    assert value("<<>?!") == 100

def test_str_numner():

    assert value("0") == 100
    assert value("10") == 100
    assert value("+10") == 100
    assert value("-10") == 100

def test_datatype():

    with pytest.raises(AttributeError):
        value(1) # checking whether error raise when inputing wrong data type
        value(0)
        value(-10)
        value(+30)






