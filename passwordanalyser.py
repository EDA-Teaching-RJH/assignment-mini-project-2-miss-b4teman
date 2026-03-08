#ANalysing the passwords

import re
import random
import string

#Class for analysing password length
class Password:
    def __init__(self, password):
        self.password = password

    def length(self):
        return len(self.password)

#Adding inheritance: inherting from password
class PasswordAnalyser(Password):

#Regular expression: importing the library (do that at the top) and checking the passwords for different features

    def uppercase(self):
        return bool(re.search(r"[A-Z]", self.password))

    def lowercase(self):
        return bool(re.search(r"[a-z]", self.password))

    def numbers(self):
        return bool(re.search(r"\d", self.password))

    def specialCharacters(self):
        return bool(re.search(r"[!-/:-@[-`{-~]", self.password))
        #How to regex ALL special characters.. 
        #https://stackoverflow.com/questions/18057962/regex-pattern-including-all-special-characters
        #look intocompiling regex

    def repeatedCharacters(self):
        return bool(re.search(r"(.)/1{2,}",self.password))

    def commonPassword(self):
        with open("commonpasswords.txt") as f:
            common = f.read().splitlines()
        
        return self.password.lower() in common

#scoring passwords + giving rating
    def score(self):
        score = 0
 
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

        if self.repeatedCharacters():
            score -= 1

        if self.commonPassword():
            score = 0

        return score

    def rating(self):
        rate = self.score()

        if rate <= 2:
            return "Weak Password"
    
        elif rate == 3:
            return "Medium Password"

        elif rate <= 4:
            return "Strong Password"

        elif rate == 5:
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

        if self.length() < 12:
            tips.append("Add more characters/Make password longer")

        return ", ".join(tips)

    def guessTime(self):
        score = self.score()

        if score <= 2:
            return "Instantly"
  
        elif score == 3:
            return "A few minutes"
    
        elif score == 4:
            return "A few hours"
    
        else:
            return "Years"
    #Change this
    
    #for reflection MD this was definitely the hardest part