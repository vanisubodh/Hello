def nestedLoops():
  for i in range(1, 4):
    print("[", end=' ')
    for j in range (1, 4):
      print("_", end=' ')
    print("]")

  persons = ["John", "Marissa", "Pete", "Dayton"]

  for person1 in persons:
    for person2 in persons:
      print(person1 + " -> " + person2)
nestedLoops()