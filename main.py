#main program

#Importing and reading passwords
from files import readPasswords, writeResults
from passwordanalyser import PasswordAnalyser
from passwordanalyser import plotEntropyDistro

passwords = readPasswords("Passwords.txt")

results = []

for p in passwords:
    analyser = PasswordAnalyser(p)

    breachCount = analyser.checkBreach()
    if breachCount > 0:
        analyser.score = lambda: 0
        analyser.rating = lambda: "Compromised"
        #lambda is used to temporarily override the score and rating because i think if its in a breach, the score should be 0

    results.append([
        p,
        analyser.score(),
        analyser.rating(),
        analyser.stars(),
        analyser.guessTime(),
        analyser.entropy(),
        analyser.suggestions(),
        breachCount #no analyser. because of lambda
    ])

writeResults("results.csv", results)
print("All Passwords Analysed")
plotEntropyDistro(passwords)

#Here the main function brings everything together

#Letting the user check their password
from passwordanalyser import PasswordAnalyser

password = input("Enter a password to check: ")
p = PasswordAnalyser(password)

breachCount = p.checkBreach()

print(f"Password: {password}")
print(f"Score: {p.score()}")
print(f"Rating: {p.rating()}")
print(f"Stars: {p.stars()}")
print(f"Guess time (years): {p.guessTime()}")
print(f"Entropy: {p.entropy()}")
print(f"Suggestions: {p.suggestions()}")

if breachCount == 0:
    print("Password not found in any breaches :D")
elif breachCount > 0:
    print(f"This password has appeared {breachCount} times in breaches.. Change it.")
else:
    print("ERROR")