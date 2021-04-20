N = 3
coffee_times = [4572, 52476, 546422, 16423, 4452, 23, 4, 53, 253, 253, 523, 1, 24, 211244]
answer = []
count = 0
fin = 0

def dfs(m, count):
    for i in range(m):
        if coffee_times[count] == 0:
            answer.append(coffee_times[count])
            dfs()

while (count < N) and (count + fin < len(coffee_times)):
    if coffee_times[count + fin] > 0:
        coffee_times[count + fin] -= 1
        count += 1
    elif coffee_times[count + fin] == 0:
        coffee_times[count + fin] -= 1
        answer.append(count + fin + 1)



print(answer)
