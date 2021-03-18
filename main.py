def listOperations():

  y = [6, 4, 2]

  y.append(12)
  y.append(8)
  y.append(4)

  y[1] = 3

  print(y)

'''
Sorting list
1. Given a list with pairs, sort on the first element
x = [ (3,6),(4,7),(5,9),(8,4),(3,1)]
2. Now sort on the second element
'''

def sortingList():
  x = [(3,6),(4,7),(5,9),(8,4),(3,1)]
  x.sort()
  print(x)

  x.sort(key = lambda x: x[1])
  print(x)
listOperations