import sys
s = sys.stdin.readlines()
if '+' in s:
    l = s.split('+')
elif '-' in s:
    l = s.split('-')
elif '*' in s:
    l = s.split('*')
elif '/' in s:
    l = s.split('/')
