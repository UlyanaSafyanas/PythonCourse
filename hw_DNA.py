f = open("text.txt")
str1 = f.readline()
f.close()

A = 0
C = 0
G = 0
T = 0

for i in str1:
    if i == "A":
        A+=1
    if i== "C":
        C+=1
    if i== "G":
        G+=1
    if i== "T":
        T+=1

print(str(A) + " " +str(C) + " " +str(G) + " " +str(T))
