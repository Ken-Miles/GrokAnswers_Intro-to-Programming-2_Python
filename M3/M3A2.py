file = open("letter.txt")
fixed = open("fixed.txt", "w")
for line in file:
  if "WOOF!" not in line:
    print(line.strip(), file=fixed)
