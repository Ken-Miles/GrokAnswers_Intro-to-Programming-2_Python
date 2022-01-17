line = input('Line: ')
split = line.split()

if 'ROBOT' in split:
  print('There is a big robot in the line.')
elif 'robot' in split:
  print('There is a small robot in the line.')
elif 'robot' in line.lower().split():
  print('There is a medium sized robot in the line.')
else:
  print('No robots here.')