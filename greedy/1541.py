import sys

input = sys.stdin.readline

compute = input().split('-')
s = 0
for i in compute[0].split('+'):
    s += int(i)
for i in compute[1:]:
    for j in i.split('+'):
        s -= int(j)

print(s)
