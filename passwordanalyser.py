#ANalysing the passwords

#Class for analysing password length
class PasswordAnalyser:
    def __init__(self, password):
        self.password = password

def length(self):
    return len(self.password)

#Regular expression: importing the library and checking the passwords for different features
import re

def uppercase(self):
    return bool(re.search(r"[A-Z]"), self.password))

def lowercase(self):
    return bool(re.search(r"[a-z]"), self.password)

def numbers(self):
    return bool(re.search(r"/d"), self.password))

def specialCharacters(self):
    return bool(re.search(r"!?<>@&%:"), self.password)
  
