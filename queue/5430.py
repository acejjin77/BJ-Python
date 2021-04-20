import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())

for i in range(n):
    rcount = 0
    commands = str(input())
    size = int(input())
    target = input()[1:-1].split(',')
    commands.replace('RR', '')

    front, back, rev = 0, 0, 0

    for command in commands:
        if command == 'R':
            rev += 1
        else:
            if rev % 2 == 0:
                front += 1
            else:
                back += 1

    if front + back <= size:
        target = target[front:size - back]
        if rev % 2 == 1:
            print('[' + ','.join(target[::-1]) + ']')
        else:
            print('[' + ','.join(target) + ']')
    else:
        print('error')
