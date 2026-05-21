s = input()
a = []
p = s.split('+')
for x in p:
  if x is not '+' and x is not '-':
    a.append(int(x))  
if '+' in s:
  total = a[0] + a[1]
if '-' in s:
  total = a[0] - a[1]
print(total)
