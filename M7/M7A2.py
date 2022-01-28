def eng2chef(string):
  if 'tion' in string:
    string = string.replace('tion','shun')
  if 'an' in string:
    string = string.replace('an','un')
  if 'th' in string:
    string = string.replace('th','z')
  if 'v' in string:
    string = string.replace('v','f')
  if 'w' in string:
    string = string.replace('w','v')
  if 'c' in string:
    string = string.replace('c','k')
  if 'o' in string:
    string = string.replace('o','oo')
  if 'i' in string:
    string = string.replace('i','ee')
  lIst = list(string)
  if lIst[-1] == '!':
    lIst[-1] = ('. bork bork bork!!')
  return(''.join(lIst))
