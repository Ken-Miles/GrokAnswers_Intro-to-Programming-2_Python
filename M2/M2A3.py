dict = {}
n = input("Car: ")
while n:
  if n in dict:
    dict[n] = dict[n] + 1
  else:
    dict[n] = 1
  n = input("Car: ")
for carKey in dict:
  print("Cars that are " + carKey + ": " + str(dict[carKey]))
