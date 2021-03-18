def rangeFunction():

  thousand = range(1, 1000)

  min = 1000
  max = 0

  for element in thousand:
    if element < min:
      min = element
      continue
    elif element > max:
      max = element
      continue

  print("max: %d" % (max))
  print("min: %d" % (min))
  
  even = []
  odd = []

  for element in range(0, 11, 2):
    even.append(element)

  for element in range(1, 11, 2):
    odd.append(element)

  print(even)
  print(odd)

rangeFunction()
