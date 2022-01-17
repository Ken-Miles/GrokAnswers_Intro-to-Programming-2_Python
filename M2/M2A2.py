dictionary = {}

n = input('Name and colour: ')

while n:
  name, number = n.split()
  dictionary[name] = number
  n = input('Name and colour: ')
for nameKey in dictionary:
  print(nameKey, dictionary[nameKey])
