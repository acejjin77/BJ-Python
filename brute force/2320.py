vowels = ["a", "o", "e", "u", "i"]

answer = 0
words = []
count = int(input()) - 1
last_word = input()
words.append(last_word)
for n in range(count):
    x = input()
    if (x in words) or (x[0] != last_word[-1]):
        for word in words:
            answer += len(word)
        break;
    else:
        words.append(x)
        last_word = x

print(answer)
