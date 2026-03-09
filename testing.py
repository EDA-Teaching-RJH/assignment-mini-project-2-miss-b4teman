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

#regex edge cases:
def testNoNumber():
    p = PasswordAnalyser("Test")
    assert p.numbers() == False

def testNoSpecialChars():
    p = PasswordAnalyser("TestPassword1245")
    assert p.specialCharacters() == False

def testRepeated():
    p = PasswordAnalyser("hehehehe1212")
    assert p.repeatedCharacters() == True

#score tets:
def testWeak():
    p = PasswordAnalyser("password")
    assert p.score() == 0

def testStrong():
    p = PasswordAnalyser("FunH4ppyT3st!!!:D")
    assert p.score() == 5

