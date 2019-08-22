
# Problem 1:
# Write some Python code that has three variables called greeting, my_name, and my_age. Intialize each of the 3 variables with an appropriate value, then print out the example below using the 3 variables and two different approaches for formatting Strings.
#
# Using concatenation and the + and 2) Using an f-string. Sample output:
# YOUR_GREETING_VARIABLE YOUR_NAME_VARIABLE!!! I hear that you are YOUR_MY_AGE_VARIABLE today!

greeting = ("Hello")
myName = ("Jessica")
age = ("34")
#
print (greeting, myName, '!!!','I hear that you are', age, 'today!' )
myGreeting = f'{greeting} {myName} !!! I hear that you are {age} today!'
print (myGreeting)
#
# # Problem 2:
# # Write some Python code that asks the user for a secret password. Create a loop that quits with the user's quit word. If the user doesn't enter that word, ask them to guess again.
#
askUser1 = input('Enter your secret password:  ')
askUser2 = input('What is your #2:  ?')
if askUser1 == askUser2:
    print("Correct")
else:
    print("Incorrect")

# Problem 3:
# Write some Python code using f-strings that prints 0 to 50 three times in a row (vertically).

x= range(1, 51, 1)
for idx in x:
    print(idx, idx, idx)




# Problem 4:
# Write some Python code that create a random number and stores it in a variable. Ask the user to guess the random number. Keep letting the user guess until they get it right, then quit.

import random

ranNumber = random.randint(1, 5)
user_guess = -1

while user_guess != ranNumber:
    user_guess = int(input("Guess random: "))
    if user_guess != ranNumber:
        print('Guess Again')
        if user_guess > ranNumber:
            print('Boom')
        else:
            print('Bang')
    else:
        print('Good Job!')