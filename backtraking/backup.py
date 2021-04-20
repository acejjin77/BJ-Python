def solution(N, coffee_times):
    answer = []

    while len(answer) < len(coffee_times):
        fin = 0
        count = 0
        while (count < N) and (count + fin < len(coffee_times)):
            if coffee_times[count + fin] > 0:
                coffee_times[count + fin] -= 1
                count += 1
            elif coffee_times[count + fin] == 0:
                coffee_times[count + fin] -= 1
                answer.append(count + fin + 1)
                fin += 1
            else:
                fin += 1

    return (answer)