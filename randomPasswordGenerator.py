from random import randint

j = 1
password_mock = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&-=+*()'

print("Random password generator!!!\n")

while (1):
  password = []
  password_length = randint(12, 18)
  password_mock_length = len(list(password_mock))
  for i in range(password_length):
    random_number = randint(0, password_mock_length - 1)
    password.append(password_mock[random_number])

  print(f'Password {j}: {"".join(password)}\n')
  j = j + 1

  enter = input("Press enter for a new password: ")