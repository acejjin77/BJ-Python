import sys

input = sys.stdin.readline
t = int(input())


def check(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1][:len(s[i])]:
            return "NO"
    return "YES"


for _ in range(t):
    phone_number = []
    n = int(input())
    for _ in range(n):
        phone_number.append(str(input()).strip())
    phone_number.sort()

    print(check(phone_number))
