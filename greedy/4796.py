import sys

input = sys.stdin.readline

case = 1
while True:
    l, p, v = map(int, input().split())

    if l == p == v == 0:
        break

    answer = (v // p) * l
    answer += min(v % p, l)

    print("Case %d: %d" % (case, answer))
    case += 1
