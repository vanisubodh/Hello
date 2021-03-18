def functions(mylist):
  summation = 0
  for num in mylist:
    summation += num
  print(summation)

def recursionFactorial(f):
    if f == 1:
      return 1
    else:
      return f * recursionFactorial(f-1)

 print(recursionFactorial(5))

  a = 2

  def scope():
    print(a)

scope()
functions(myList)
recursionFactorial(f)