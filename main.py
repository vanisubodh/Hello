#Printin random numbers in range

import random

def randomNumbers():
  x = random.randint(0, 10)

  print(x)

  print("")

  i = 0

  while(i<3):

    print(random.randint(0, 100))

    i += 1

  i = 0

  print("")

  numberOccurances = {}

  while (i < 100):

    rand = random.randint(0,100)

    if(rand not in numberOccurances):
      numberOccurances[rand] = 1
    else:
      numberOccurances[rand] += 1

    i += 1

  print(numberOccurances)
randomNumbers()