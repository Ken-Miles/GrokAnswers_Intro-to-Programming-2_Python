def fix_yz(x):
  x=x.replace('z','$$IfYoUsEeThIsItIssAbbUUUuug$$')
  x=x.replace('Z','$$IfYoUsEeThIsItIssAbbUUUuuug$$')
  x=x.replace('y','z')
  x=x.replace('Y','Z')
  x=x.replace('$$IfZoUsEeThIsItIssAbbUUUuug$$','y')
  x=x.replace('$$IfZoUsEeThIsItIssAbbUUUuuug$$', 'Y')
  return(x)
