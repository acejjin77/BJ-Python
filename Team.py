count = 0
for n in range(int(input())):
    a,b,c = input().split(" ")
    a,b,c = int(a),int(b),int(c)
    if (a+b+c > 1):
        count += 1

print(count)
