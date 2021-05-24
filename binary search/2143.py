import sys

input = sys.stdin.readline

t = int(input())
len_a = int(input())
a = list(map(int, input().split()))
len_b = int(input())
b = list(map(int, input().split()))
answer = 0

a.sort()
b.sort()

for i in range(1, len_a + 1):
    s = 0
    e = len_b
    while s <= e:
        newb = b[s:e]
        calc = sum(a[:i]) + sum(newb[:e])
        print(s, e, calc,  a[:i], newb[:e])
        if calc < t:
            s += 1
        elif calc > t:
            e -= 1
        if calc == t:
            answer += 1
            s += 1

    print(answer)
