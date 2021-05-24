
record = input()

answer = []
stack = []
for s in record:
    change = 0
    c, uid, nick = s.split(" ")[0], s.split(" ")[1], s.split(" ")[2]
    if c == 'Enter':
        answer.append(nick + "님이 들어왔습니다.")
        stack.append([uid, 1])
        for sss in stack:
            if uid == sss[0]:
                change = 1
    elif c == 'Leave':
        answer.append(nick + "님이 나갔습니다.")
        stack.append([uid, 0])

    if c == 'Change' or change:
        for i in range(len(stack)):
            if uid == stack[i][0]:
                if stack[i][1]:
                    answer[i] = nick + "님이 들어왔습니다."
                else:
                    answer[i] = nick + "님이 나갔습니다."


print(answer)