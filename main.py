#main program

#Importing and reading passwords
from files import readPasswords
passwords = readPasswords("Passwords.txt")

for p in passwords:
    print(p)

analyser = passwordAnalyser(p)
print(analyser.length())

from files import readPasswords, writeResults
from passwordanalyser import PasswordAnalyser

password = readPassword("Passwords.txt")

results = []

for p in passwords:

    analyser = PasswordAnalyser(p)

    results.append([
        p,
        analyser.score(),
        analyser.rating(),
        analyser.guessTime(),
        analyser.suggestions()
    ])

writeResults("results.csv", results)
print("All Passwords Analysed")

#Here the main function brings everything together