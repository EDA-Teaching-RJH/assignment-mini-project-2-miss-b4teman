#Importing csv library, reading and opening passwords.txt, removing whitespace
import csv

def readPasswords(filePath):
    with open(filePath) as file:
        passwords = [line.strip() for line in file]

    return passwords


#Writing the results to my results csv file using all results from the passwordanalyster, the O in file i/o
def writeResults(filePath, results):

    with open(filePath, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Password ",
            "Score ",
            "Rating ",
            "Stars ",
            "Guess time (Years) ",
            "Entropy ",
            "Suggestions "
        ])

        for r in results:
            writer.writerow(r)