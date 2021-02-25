for n in range(int(input())):
    output = input()
    leng = len(output)
    if leng > 10:
        leng -= 2
        output = output[:1] + str(leng) + output[-1:]
    print(output)

