'''
print("What is 13*6: ")
condition = True
while condition:
    i = int(input("Enter your answer: "))
    if i==13*6:
        print("Correct answer")
        condition = False
    else:
        print("Incorrect answer, try again")
        i = int(input("Enter your answer: "))
'''

'''

'''

lives = 5
random = 2
condition = True
print("Guess a number that is between 0 to 9.\nYou have 5 lives")
while lives!=0 and condition:
    userInput = int(input("Enter the number: "))
    if userInput ==random:
        print("Congrats!! Correct guess")
        condition = False
    else:
        lives-=1
        print("Oopes.. Wrong ans", lives, "lives remaining")
        userInput = int(input("Enter the number: "))