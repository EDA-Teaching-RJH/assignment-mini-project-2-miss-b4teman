#testing to test diff other passwords
import pytest
from passwordanalyser import PasswordAnalyser

#testing diff features:
def testLength():
    p = PasswordAnalyser("HelloTest!!!!")
    assert p.length() == 12

def testUppercase():
    p = PasswordAnalyser("Testingg")
    assert p.uppercase() == True

def testLowercase():
    p = PasswordAnalyser("tEsTiNg")
    assert p.lowercase() == True

def testNumbers():
    p = PasswordAnalyser("test67")
    assert p.numbers() == True

def testSpecial():
    p = PasswordAnalyser("Test:P")
    assert p.specialCharacters() == True