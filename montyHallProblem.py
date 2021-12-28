# Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

# Vos Savant's response was that the contestant should switch to the other door.[3] Under the standard assumptions, the switching strategy has a 2/3 probability of winning the car, while the strategy that remains with the initial choice has only a 1/3 probability.

from random import randint

entries = int(input("Número de casos de teste: "))

sum_values = 0

for i in range(entries):
  user_guess = randint(0, 2)
  answer = randint(0, 2)
  
  if user_guess == answer:
    sum_values = sum_values + 1

unchanged_score = entries - sum_values


print(f"Você que não mudou nenhuma porta acertou {sum_values} vezes, um total de {(sum_values / entries) * 100}%")
print(f"Caso tenha mudado iria acertar {unchanged_score} vezes, um total de {(unchanged_score / entries) * 100}%")
    
