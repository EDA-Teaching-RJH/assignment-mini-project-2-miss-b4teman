#testing to test diff other passwords
import pytest
from passwordanalyser import PasswordAnalyser

#testing diff features:
def test_Length():
    p = PasswordAnalyser("HelloTest!!!!")
    assert p.length() == 12

def test_Uppercase():
    p = PasswordAnalyser("Testingg")
    assert p.uppercase() == True

def test_Lowercase():
    p = PasswordAnalyser("tEsTiNg")
    assert p.lowercase() == True

def test_Numbers():
    p = PasswordAnalyser("test67")
    assert p.numbers() == True

def test_Special():
    p = PasswordAnalyser("Test:P")
    assert p.specialCharacters() == True

#regex edge cases:
def test_NoNumber():
    p = PasswordAnalyser("Test")
    assert p.numbers() == False

def test_NoSpecialChars():
    p = PasswordAnalyser("TestPassword1245")
    assert p.specialCharacters() == False

def test_Repeated():
    p = PasswordAnalyser("hehehehe1212")
    assert p.repeatedCharacters() == True

#score tets:
def test_Weak():
    p = PasswordAnalyser("password")
    assert p.score() == 0

def test_Strong():
    p = PasswordAnalyser("FunH4ppyT3st!!!:D")
    assert p.score() == 5

#entropy test:
def test_GoodEntropy():
    p = PasswordAnalyser("Test?@12LOLc4t")
    assert p.entropy() > 0

def test_Empty():
    p = PasswordAnalyser("")
    assert p.entropy() == 0

#Testing the code:
def test_Code():
    try:
        p = PasswordAnalyser("")
        p.score()
        p.entropy()
        p.rating()

    except Exception:
        pytest.fail("ERROR: Empty password")