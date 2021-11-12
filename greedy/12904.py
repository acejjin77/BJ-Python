import sys

s = list(map(str, input()))
t = list(map(str, input()))

while len(s) != len(t):
    if t[-1] == "A":
        t.pop()
    else:
        t.pop()
        t = t[::-1]
    
if s == t:
    print(1)
else:
    print(0)