n, k = map(int, input().split())
num = list(input())
result = []

while (k > 0):
    if (k == len(num)):
        num = []
        break
    print(num[:k+1], result, k)
    i = num.index(max(num[:k+1]))
    result.append(num[i])
    num = num[i+1:]
    k -= i
result += num
print("".join(result))
