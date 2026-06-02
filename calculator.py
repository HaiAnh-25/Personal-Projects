import sys
import calcobj.py
s = sys.stdin.readlines()
if '+' in s:
    l = s.split('+')
elif '-' in s:
    l = s.split('-')
elif '*' in s:
    l = s.split('*')
elif '/' in s:
    l = s.split('/')
