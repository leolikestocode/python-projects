from random import randint

max_value = int(input("Type the max value of the guessing 'the number' game: "))
lower = 1
higher = max_value
computer_number = randint(lower, higher)

print(f"Now think about a number between 1 and {max_value} and see if the computer guessed it")
aux = input("Press enter to start the game:")

while (computer_number):
    ipt = input(f"The computer guessed {computer_number}. Is it lower(L), higher(H) or correct(C)? \n")
    if (ipt.lower() == "l"):
      lower = computer_number + 1
    elif (ipt.lower() == "h"):
      higher = computer_number - 1
    elif (ipt.lower() == "c"):
      break
    computer_number = randint(lower, higher)

print(f"Hoooooorray the computer got it right, the correct number is {computer_number}!!!")