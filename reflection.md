OCF2 Sola Fayemi
Fundamentals of Programming: Mini project 2
Developer Journal

Regular Expressions (REGEX):
(Workshop 8) In this workshop, I was introduced to multiple different uses for REGEX. This was particularly useful for my code as I'm analysing passwords and this makes it significantly easier, especially for my function that detects repeated characters like 'aaaa'. 

Testing:
(Lecture 8, Workshop 8) I learnt that its good to 'segment tests into their own functions', and I have demonstrated this by making a function for each feature of the password that was being tested i.e. special characters, numbers etc. A useful feature note from workshop 8 which I utilised is using using assert instead of an if statement for things I think to be true, which I have done so in test_PasswordAnalyser.py. Another thing I learnt and utilised from the workshop, is using Try and Except to test an edge case, which I did for empty passwords.

Libraries:
(Lecture 7) I learnt that libraries are 'chunks of code which you can reference in your program to give you more functionality'. In my code, I have demonstrated this by importing passwordanalyser.py and files.py into main.py. I was able to import specific modules, in this case, 'readPasswords' and 'writeResults' were modules that were imported from files.py, and 'PasswordAnalyser' was the module imported from passwordanalyser.py.

File I/O:
(Lecture 8) This lecture was particularly useful for reading and writing from files, and choosing the file to be read/written from, as well as specifically using 'with', in my code, I have the line 'with open(filePath, "w", newline="") as file:'. I used a csv file, meaning I had to also import csv. 

Object-Oriented Programming (OOP):
(Workshop 9/Lecture 9) This lecture and workshop introduced OOP concepts, including classes and inheritance. In my code, I have my base class as 'Password' and my child class as 'PasswordAnalyser'. From the workshop, I was taught how to 'implement a constructor (init method), which I have made use of in my own code.

Above and Beyond:
I decided to add multiple features. I added a matplotlib graph to show what the entropy score distribution looks like. I chose entropy as I feel like that's the most important feature. I also added an estimated guess time in years, and I searched and found that a modern computer can do 100billion guesses/second, but when I did that, I was left with really big numbers, so I changed it to years. I also added a list of the 50 most common passwords as a txt file, so that I could detect what passwords in my list are common passwords. Ideally, I'd have liked to check for passwords found in breaches from haveibeenpwned, however I did find that a little difficult.

Development Process:
The first step in my development process was planning what my program should be. I had decided to do a password analyser as I felt that I would be able to fit all of the criteria into this one program. I wanted to check for the length, uppercase and lowercase letters, numbers and special characters, as this would demonstrate my understanding of REGEX. I also added checking for repeated characters and whether the password is a common password. This would then give a score, I later added a rating and estimated guess time based off of the entropy, something I had learnt about looking at other password analyser tools online. To calculate entropy, I based it off of length, upper and lowercase letters, special characters and numbers, although entropy can be also affected by using recognisable words/phrases. The formula for entropy is E = L × log2(R), where E = Entropy, R is the range of character types in the password, L is the password length. The program would then read passwords from, 'Passwords.txt' and writes the results to 'results.csv'. I also wanted to detect common passwords, so I found a list and created a .txt file of them.
I firstly created a draft to understand the layout of my code. The crucial part of my code is found in 'passwordanalyser.py' as it defines 2 classes: Password, which is the base class that stores the password and its length, and PasswordAnalyser, which inherits from Password and then performs the full analysis. It checks different features using REGEX, calculates the score, rating, entropy, guess time and provides improvement suggestions.
'files.py' handles the file I/O. It has 2 functions, 'readPasswords' which reads the passwords from the txt file and removes whitespace, and 'writeResults' which writes the results to a csv file. 
'main.py' connects all of my program together, it reads the passwords, creates a 'PasswordAnalyser' object for each password, stores that in a list and writes the results to the 'results.csv'. I also added a feature which allows a user to check their own password directly in the terminal. 
I also had to import modules to be able to perform the functions I wanted in my code, for example math. I also imported my own custom libraries, as shown in main.py. 
'test_PasswordAnalyser' is used to check test that my code works, as well as testing edge cases, for my tests, I used an empty password, the entropy, different scores and for different features.



