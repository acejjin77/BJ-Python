word = input()
search = input()
cnt = 0

while (len(search) <= len(word)):
    if (search == word[:len(search)]):
        cnt += 1
        word = word[len(search):]
    else:
        word = word[1:]

print(cnt)