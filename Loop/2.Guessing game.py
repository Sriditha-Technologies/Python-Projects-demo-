import random

def guessing_game():
    number_to_guess=random.randint(1 ,10)
    attempts=0
    while True:
      guess=int(input("Enter the number(between 1 and 10): "))
      attempts +=1

      if guess < number_to_guess:
         print("To Low! Try Again")
      elif guess > number_to_guess:
         print("To High! Try Again")
      else:
         print(f"Congradulation! Your are the guessing {attempts}.")
         break
guessing_game()


