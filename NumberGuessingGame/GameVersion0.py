import random
print("Hey there, Welcome to the game!")
print("I am thinking of a number between 1 and 100.")
print("Can you guess the number? You have 4 attempts")
number = random.randrange(1,100)
guessed = False
for i in range(4):
    guess = int(input("Enter your guess:"))
    if(guess > number):
        print("Sorry, Too High")    
    elif(guess < number):
        print("Sorry, Too Low")
    else:
        print(f"Correct! You got it in {i} attempts.Well done.")  
        guessed = True         
        break
if not guessed:
    print("Oops! Better luck next time.") 