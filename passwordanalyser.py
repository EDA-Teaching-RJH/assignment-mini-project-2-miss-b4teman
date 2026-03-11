#ANalysing the passwords

#Importing modules needed
import re
import math
import matplotlib.pyplot as plt
import hashlib 
import requests



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
        return bool(re.search(r"[^\w\s]", self.password))

    def repeatedCharacters(self):
        return bool(re.search(r"(.)\1{2,}",self.password))

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

        if self.commonPassword():
            tips.append("Common Password")

        if self.repeatedCharacters():
            tips.append("Remove repeated characters")

        return ", ".join(tips)

    def guessTime(self):
        entropy = self.entropy()
        guesses = 2 ** entropy
        guessesPerSecond = 100000000000 #Actual number computers can do
        seconds = guesses / guessesPerSecond
        years = seconds / (60 * 60 * 24 * 365)

        return round(years, 2)
    
    #for reflection MD this was definitely the hardest part

    def stars(self):
        score = self.score()

        givenStars = "★" * score
        missing = "☆" * (5 - score)

        return givenStars + missing

    def entropy(self):

        pool = 0

        if self.lowercase():
            pool += 26

        if self.uppercase():
            pool += 26

        if self.numbers():
            pool += 10

        if self.specialCharacters():
            pool += 32

        if pool == 0:
            return 0

        entropy = self.length() * math.log2(pool)
        return round(entropy, 2)

    #26 is because there are 26 letters A-Z, 10 is because there are 10 digits, and 32 is because there are 32 special characters

    #attempting to check if password appears in data breaches
    def checkBreach(self):
        #sha 1 hash of the passwords, i.e 'k anonimity', upper() because the haveibeenpwned API hashes are uppercase
        sha1Password = hashlib.sha1(self.password.encode()).hexdigest().upper()

        prefix = sha1Password[:5]
        suffix = sha1Password[5:]

        url = f"https://api.pwnedpasswords.com/range/{prefix}"

        try:
            response = requests.get(url)
            if response.status_code != 200:
                print("Error")
                return -1
            
            hashes = (line.split(":") for line in response.text.splitlines())

            for h, count in hashes:
                if h == suffix:
                    return int(count) #password was found in databreach
                
            return 0 #password wasnt found
        
        except Exception as e:
            print("ERROR: API:", e)
            return -1





#matplotlib visualisation:
def plotEntropyDistro(passwords):
    entropies = []

    for pw in passwords:
        analyser = PasswordAnalyser(pw)
        entropies.append(analyser.entropy())

    plt.figure(figsize=(8,5))

    plt.hist(entropies, bins = 10, color = "#f45cff", edgecolor = "#11004a")
    
    plt.title("Entropy Score Distribution")
    plt.xlabel("Entropy Score")
    plt.ylabel("No. of Passwords")

    plt.grid(axis = "y", linestyle = "dashed", alpha = 1)

    plt.tight_layout()
    plt.savefig("Entropy Distribution.png")
    plt.show()