from random import randint

max_value = int(input("Type the max value of the guessing 'the number' game: "))

guessing_number = int(input(f"Guess a number between 1 and {max_value}: "))
the_number = randint(1, max_value)

while (guessing_number != the_number):
  if (guessing_number > the_number):
    print("Hmmm, to high! The number is lower than that\n")
  if (guessing_number < the_number):
    print("Hmmm, to low! The number is higher than that\n")
  if (guessing_number != the_number):
    guessing_number = int(input("Guess another number: "))

print(f"Hoooooorray you got it right, the correct number is {the_number}!!!")