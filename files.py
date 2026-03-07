#Importing csv library, reading and opening passwords.txt, removing whitespace
import csv

def readPasswords(filePath):
    with open(filePath):
        passwords = [line.strip() for line in file]

    return passwords

