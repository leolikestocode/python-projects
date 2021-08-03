from random import randint
import time

min = 1
max = 10000000

num = randint(min, max)
print(num)
print()

# Increasing
start_time = time.time()
for i in range(min, max):
  if (i == num):
    break

print("Increasing %s seconds" % (time.time() - start_time))

# Decreasing
start_time = time.time()
for i in range(max, min, -1):
  if (i == num):
    break

print("Decreasing %s seconds" % (time.time() - start_time))

# Binary Search
start_time = time.time()
bmax = max
bmin = min
bnum = round((bmin + bmax) / 2)

while (1):
  if (bnum == num):
    break

  if (bnum < num):
    bmin = bnum
  else:
    bmax = bnum

  bnum = round((bmin + bmax) / 2)


print("Binary Search %s seconds" % (time.time() - start_time))
