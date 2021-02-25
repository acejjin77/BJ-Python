word = input().lower()

vowels = ["a","o","y","e","u","i"]

output = ""
for n in word:
    if (n not in vowels):
        output += "." + n
print (output)
