from plates import is_valid
import pytest

def test_default():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    



def test_length():
    
    assert is_valid("ABCS50") == True
    assert is_valid("CS") == True
    assert is_valid("CS50") == True

    assert is_valid("") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("C") == False
    assert is_valid("CS59999") == False

def test_first_2_letter():

    assert is_valid("ABCD") == True
    assert is_valid("TH150") == True
    
    assert is_valid("50CS") == False
    assert is_valid("5CS") == False

def test_middle_number():

    assert is_valid("HI134") == True
    assert is_valid("AB0") == True
    
    assert is_valid("CS050") == False

    assert is_valid("CS50T") == False
    assert is_valid("CS50T") == False
    assert is_valid("AB1T40") == False

def test_punctuation_space():

    assert is_valid("AB CD") == False
    assert is_valid("CS,50") == False

def test_data_type():

    with pytest.raises(TypeError):
        is_valid(0) #Wrong data type
        is_valid(506)





