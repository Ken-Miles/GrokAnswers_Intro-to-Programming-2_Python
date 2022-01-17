dict1 = {}
dict2 = {}
n = input("Enter line: ").split()
while n:
  for testloop in range(len(n)):
    if n[testloop] in dict1:
      dict1[n[testloop]] = dict1[n[testloop]] + 1
    else:
      dict1[n[testloop]] = 1
  dict2.update(dict1)
  n = input("Enter line: ").split()
for i in sorted(dict2):
  print(i, dict2[i])
