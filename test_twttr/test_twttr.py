from twttr import shorten
import pytest

def test_shorten_name():

    assert shorten("throshan") == "thrshn"
    assert shorten("VenUjan") == "Vnjn"
    assert shorten("Niruthigan") == "Nrthgn"

def test_punctuation():
    assert shorten("./<>") == "./<>"
    assert shorten("hello<..?'") == "hll<..?'"

def test_shorted_str_num():

    assert shorten("0")
    assert shorten("1") == "1"
    assert shorten("1344") == "1344"


def test_datatype():
    with pytest.raises(TypeError):
        shorten(10) #inserting non str value
        shorten(1.4)
