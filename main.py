def whileLoops():
  clist = ["Canada","USA","Mexico"]
  i = 0

  while(i < len(clist)):
    print(clist[i], end=' ')
    i += 1

  print("")

  i = 1
  summation = 0

  while(i in range(1,11)):
    summation += i
    i += 1
  print(summation)
whileLoops()
