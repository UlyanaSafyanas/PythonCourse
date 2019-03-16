f = open("text.txt")
str1 = f.readline()
f.close()

str2 = ""

for i in str1:
    if i== "T":
        str2+="U"
    else:
        str2+=i

print(str2)
