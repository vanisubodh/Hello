def readFile():

  file = open("txt.txt", "r")

  i = 1

  for line in file:
    print("%d %s" % (i, line), end='')
    i += 1

  print("")

  file.close()
readFile()