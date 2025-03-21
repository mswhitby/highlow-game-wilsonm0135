import random

def main():
    secret_number = random.randint(1,13)
    max_guesses = 7
    num_guesses=0
    print("welcome to my number guessing game:3")
    print("im thinking of a number between 1 and 13. You have{max_guesses}guesses to guess it")
    
    while num_guesses < max_guesses:
      guess= int(input("Enter your guess:'"))
      num_guesses += 1
    
    
    if guess == secret_number:
      print ("!!!congratulations! you guesses the right number in{num_guesses}guesses.")
    
    if guess < secret_number:
      print("Too low! guess higher.")
    else:
      print("Too high guess lower.")

main()
