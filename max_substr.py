problem = input("string anything")
substr_list = []
substr = ""
temp = ""

def add(l, r):
    return  l + r

for i in range(len(problem)):
    if problem[i] in substr:
        substr_list.append(substr)
        substr = problem[i]
    else:
        substr += problem[i]

for i in range(len(substr_list)):
    if len(substr_list[i]) > len(temp):
        temp = substr_list[i]

print(temp)
