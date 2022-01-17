file = open("book.txt").read().lower()
n = input("Word to look for: ")
if n in file:
  print(n, "was found in the book.")
else:
  print(n, "was not found in the book.")