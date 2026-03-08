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
    return bool(re.search(r"[!-\/:-@[-`{-~]"), self.password)
    #How to regex ALL special characters.. 
    #https://stackoverflow.com/questions/18057962/regex-pattern-including-all-special-characters
    #look intocompiling regex

#scoring passwords + giving rating
def score(self)
    score = o
 
    if self.length() >= 8:
        score += 1
    
    if self.uppercase():
        score += 1

    if self.lowercase():
        score += 1

    if self.numbers():
        score += 1

    if self.specialCharacters():
        score += 1

    return score

def rating(self):
    rate = self.score()

    if rate <= 2:
        return "Weak Password"
    
    elif rate == 3:
        return "Medium Password"

    elif rate <= 4:
        return "Strong Password"

    elif rate < 4:
        return "Very Strong Password"

    else:
        return "ERROR"

#Suggestions for password, tips is empty, but if it doesnt fit a criteria it will add the related suggestion
def suggestions(self):
    
    tips = []
    
    if not self.uppercase():
        tips.append("Add uppercase letters")

    if not self.numbers():
        tips.append("Add numbers")

    if not self.specialCharacters():
        tips.append("Add special characters")

    if not self.length() < 12:
        tips.append("Add more characters/Make password longer")

    return "".join(tips)
