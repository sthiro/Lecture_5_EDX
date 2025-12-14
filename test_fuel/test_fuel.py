from fuel import convert, gauge
import pytest


def test_default():

    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    assert convert("0/4") == 0


def test_zero_division_error():

    with pytest.raises(ZeroDivisionError):
        convert("4/0")


def test_text_error():

    with pytest.raises(ValueError):
        convert("three/four")
        # convert("1.5/3")
        # convert("5/4")


def test_decimal_error():

    with pytest.raises(ValueError):
        convert("1.5/3")
        # convert("5/4")

def test_XgreaterThanY_error():

    with pytest.raises(ValueError):
        convert("5/4")


def test_negative_value():

    with pytest.raises(ValueError):
        convert("-3/4")


def test_gauge():

    assert gauge(1) == "E"
    assert gauge(0) == "E"

    assert gauge(100) == "F"
    assert gauge(99) == "F"

    assert gauge(80) == "80%"










