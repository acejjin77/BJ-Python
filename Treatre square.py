n, m, a = map(int,input().split())
r1, r2 = int(n/a), int(m/a)

if(n%a != 0):
    r1 += 1
if(m%a != 0):
    r2 += 1

print(r1*r2)