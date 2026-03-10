#main program

#Importing and reading passwords
from files import readPasswords, writeResults
from passwordanalyser import PasswordAnalyser

passwords = readPasswords("Passwords.txt")

results = []

for p in passwords:
    analyser = PasswordAnalyser(p)

    results.append([
        p,
        analyser.score(),
        analyser.rating(),
        analyser.stars(),
        analyser.guessTime(),
        analyser.entropy(),
        analyser.suggestions()
    ])

writeResults("results.csv", results)
print("All Passwords Analysed")

#Here the main function brings everything together

#Letting the user check their password
from passwordanalyser import PasswordAnalyser

password = input("Enter a password to check: ")
p = PasswordAnalyser(password)

print(f"Password: {password}")
print(f"Score: {p.score()}")
print(f"Rating: {p.rating()}")
print(f"Stars: {p.stars()}")
print(f"Guess time (years): {p.guessTime()}")
print(f"Entropy: {p.entropy()}")
print(f"Suggestions: {p.suggestions()}")

