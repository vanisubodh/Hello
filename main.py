def forLoops():
  clist = ['Canada','USA','Mexico','Australia']

  for listing in clist:
    print(listing)

  for num in range(0,100):
    print(num, end=' ')

  print("")

  for mult1 in range(1,13):
    for mult2 in range(1, 13):
      print(mult1 * mult2, end=' ')

    print("")

  for num in range(10, 1):
    print(num, end=' ')

  print("")

  for num in range(0, 10):
    if(num % 2 == 0):
      print(num, end=' ')

  print("")

  summation = 0
  for num in range(100, 200):
    summation += num

  print(summation)
forLoops()
