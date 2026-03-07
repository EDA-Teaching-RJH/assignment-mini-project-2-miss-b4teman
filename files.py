#Importing csv library, reading and opening passwords.txt, removing whitespace
import cvs

def readPasswords(filePath):
    with open(filePath):
        passwords = [line.strip() for line in file]

    return passwords

