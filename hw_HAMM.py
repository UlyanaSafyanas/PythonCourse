f = open("text.txt")
str1 = f.readline()
str2 = f.readline()
f.close()
Q=0

for i in range(len(str2)):
    if str1[i]!=str2[i]:
        Q+=1

print(str(Q))
        
