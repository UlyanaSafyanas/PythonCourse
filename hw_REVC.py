f = open("text.txt")
str1 = f.readline()
f.close()

str2 = ""


for i in str1:
    if i == "A":
        str2+="T"
    if i== "C":
        str2+="G"
    if i== "G":
        str2+="C"
    if i== "T":
        str2+="A"

str2=str2[::-1]




print(str2)
