#Rock paper scissors python

import random

rps = ['r', 'p', 's']
count = 0
compscore = 0
userscore = 0

playtime = int(input("Enter the number of times you want to play this game"))



while count<playtime:
    compguess = random.choice(rps)
    userguess = input("Enter 'r' for rock, 'p' for paper and 's' for scissors").lower()
    if userguess not in rps:
        print("Invalid, try again")
        continue
    if userguess == compguess:
        compscore += 0
        userscore +=0
        print("Draw, the score is", userscore,"-", compscore, "(User-Computer)")
    elif userguess == 'r' and compguess == 's':
        compscore +=0
        userscore += 1
        print("You win, the score is", userscore,"-", compscore, "(User-Computer)")
    elif userguess == 'p' and compguess == 'r':
        compscore +=0
        userscore += 1
        print("You win, the score is", userscore,"-", compscore, "(User-Computer)")
    elif userguess == 's' and compguess == 'p':
        compscore +=0
        userscore += 1
        print("You win, the score is", userscore,"-", compscore, "(User-Computer)")
    elif userguess == 'r' and compguess == 'p':
        compscore +=1
        userscore += 0
        print("Computer wins, the score is", userscore,"-", compscore, "(User-Computer)")
    elif userguess == 'p' and compguess == 's':
        compscore +=1
        userscore += 0
        print("Computer wins, the score is", userscore,"-", compscore, "(User-Computer)")
    elif userguess == 's' and compguess == 'r':
        compscore +=1
        userscore += 0
        print("Computer wins, the score is", userscore,"-", compscore, "(User-Computer)")
    count+=1

print("The total score is", userscore, "-", compscore)
    


    
