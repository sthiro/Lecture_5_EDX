from twttr import shorten
import pytest

def test_shorten_name():

    assert shorten("Throshan") == "Thrshn"
    assert shorten("Venujan") == "Vnjn" 
    assert shorten("Niruthigan") == "Nrthgn"

def test_shorted_str_num():

    assert shorten("1") == "1"
    assert shorten("1344") == "1344"


def test_datatype():
    with pytest.raises(TypeError):
        shorten(10) #inserting non str value
        shorten(1.4)