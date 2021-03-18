def scopeAlso():

  x = 100

  def reduce(x):
    global y
    y = x - 50

  reduce(x)

  print(y)
scopeAlso()