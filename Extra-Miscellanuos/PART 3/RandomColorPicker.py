import random

colors = ['maroon', 'red', 'teal', 'orange', 'green', 'blue', 'purple', 'violet']

print(colors)

while True:
    guess = input("Pick a color from the list given above: ")
    color = colors[random.randint(0, len(colors)-1)]

    while True:
        if(color == guess.lower()):
            break
        else:
            guess = input("Nope, Try again: ")
    
    print("Congratulations! I was thinking about the color", color)
                   
    play_again = input("Do you want to play again? Type 'no' to quit: ")

    if(play_again.lower() == "no"):
        break

print("Thanks for playing!")

