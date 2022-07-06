import random

number = random.randint(1,10)
guess = round(float(input("I am thinking a number. Can you guess what that number is? ")),0)

while True:
    if( guess == number):
        print("Congratulations! You guessed the number")
        break;
    else:
        guess = round(float(input("Nope, not the number i am thinking of ")),0)
        
