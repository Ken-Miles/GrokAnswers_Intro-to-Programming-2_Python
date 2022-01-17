file = open("input.txt").read().lower()
file = file.split("\n")
final = []
counter = 0
counter2 = -1
for line in file:
  counter = counter + 1
  if line.count("a") >= 3 and line.count("r") >= 2 and line.count("d") >= 1 and line.count("v") >= 1 and line.count("k") >= 1:
    final.append(counter)
for numbers in final:
  counter2 = counter2 + 1
  print("Aardvark on line", final[counter2])
