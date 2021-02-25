x = input()
n, k = x.split(" ")
n, k = int(n), int(k)
score_array = input().split(" ")
count = 0
for num in range(n):
    score = int(score_array[num])
    if (score > 0 and score >= int(score_array[k-1])):
        count += 1
print(count)