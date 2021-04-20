string = str(input())
strings = []
for i in range(len(string)):
    for j in range(len(string) - i):
        strings.append(string[j:j + i + 1])

answer = []
for s in set(strings):
    dup = []*len(s)
    for i in s:
        if i not in dup:
            dup.append(i)
        else:
            break
        if ''.join(dup) == s:
            answer.append(s)

print(len(answer))