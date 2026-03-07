#main program
#Importing and reading passwords
from files import readPasswords
passwords = readPasswords("Passwords.txt")

for p in passwords:
    print(p)