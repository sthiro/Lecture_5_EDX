from twttr import shorten

def test_shorten():
    assert shorten("Throshan") == "Thrshn"
    assert shorten("Venujan") == "" 
