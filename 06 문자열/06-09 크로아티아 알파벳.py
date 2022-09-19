apb = ['c=','c-','dz=','d-','lj','nj','s=','z=']
a=input()
for i in apb:
  for i in apb:
    if a.find(i) != -1:
     a = a.replace(i, '0', 1)
print(a)