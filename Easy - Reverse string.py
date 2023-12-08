
def solulu(s):

    i, j = 0, len(s) - 1

    while i < j:
        s[i],s[j] = s[j], s[i]
        i+=1
        j-=1

s = ["H","a","n","n","a","h"]

print(s)
solulu(s)
print(s)