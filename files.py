#Importing csv library, reading and opening passwords.txt, removing whitespace
import csv

#function for reading the file that contains the passwords, and opening it with each password as a line so they can be used
def readPasswords(filePath):
    with open(filePath) as file:
        passwords = [line.strip() for line in file]

    return passwords


#Writing the results to my results csv file using all results from the passwordanalyser, the O in file I/O. 
def writeResults(filePath, results):

    with open(filePath, "w", newline="") as file:

        writer = csv.writer(file)

        #writing the results and having a row for each result
        writer.writerow([
            "Password",
            "Score",
            "Rating",
            "Stars",
            "Guess time (Years)",
            "Entropy score (Bits)",
            "Suggestions",
            "Breach count"
        ])

        for r in results:
            writer.writerow(r)