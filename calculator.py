import sys
import calcobj
s = sys.stdin.readlines()
s = s[0].strip()
l = []
if '+' in s:
    l = s.split('+')
elif '-' in s:
    l = s.split('-')
elif '*' in s:
    l = s.split('*')
elif '/' in s:
    l = s.split('/')
m = int(l[0])
n = int(l[1])

if '+' in s:
    print(m + n)
elif '-' in s:
    print(m - n)
elif '*' in s:
    print(m * n)
elif '/' in s:
    print(m / n)