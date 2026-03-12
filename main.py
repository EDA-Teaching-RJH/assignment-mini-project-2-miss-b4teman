#main program
#to run the code: type 'python3 main.py into the terminal as this is a virtual space, it struggles with matplotlib
#also please make sure 'python' and 'rainbow csv' is installed !

#Importing and reading the functions/libraries for reading the passwords, getting the results, analysing them, and for the entropy graph
from files import readPasswords, writeResults
from passwordanalyser import PasswordAnalyser
from passwordanalyser import plotEntropyDistro

#reading the passwords
passwords = readPasswords("Passwords.txt")

results = []

#analysing the passwords to get the results
for p in passwords:
    analyser = PasswordAnalyser(p)

    #changing the score and rating to 0 for the password if it has been found in a breach
    breachCount = analyser.checkBreach()
    if breachCount > 0:
        analyser.score = lambda: 0
        analyser.rating = lambda: "Compromised"
        #lambda is used to temporarily override the score and rating because I decided that if its in a breach, the score should be 0

    #appending the results list with each feature for all the passwords
    results.append([
        p,
        analyser.score(),
        analyser.rating(),
        analyser.stars(),
        analyser.guessTime(),
        analyser.entropy(),
        analyser.suggestions(),
        breachCount #no 'analyser.' because of lambda
    ])

#writing the results to the csv file, and sending message to the terminal to say all passwords analysed.
writeResults("results.csv", results)
print("All Passwords Analysed")
plotEntropyDistro(passwords)

#Letting the user check their own password with the same metrics the passwords from my txt file  have been analysed with
from passwordanalyser import PasswordAnalyser

password = input("Enter a password to check: ")
p = PasswordAnalyser(password)

breachCount = p.checkBreach()

#printing the results of the users password for each metric
print(f"Password: {password}")
print(f"Score: {p.score()}")
print(f"Rating: {p.rating()}")
print(f"Stars: {p.stars()}")
print(f"Guess time (years): {p.guessTime()}")
print(f"Entropy: {p.entropy()}")
print(f"Suggestions: {p.suggestions()}")

#checking if the users password has appeared in any breached
if breachCount == 0:
    print("Password not found in any breaches :D")
elif breachCount > 0:
    print(f"This password has appeared {breachCount} times in breaches.. Change it.")
else:
    print("ERROR")