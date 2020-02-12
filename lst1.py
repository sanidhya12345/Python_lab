l=list(input().split())
c=[]
for i in l:
       if i not in c:
             c.append(i)
for i in range(len(c)-1):
           print(c[i],end="*")
print(c[len(c)-1])
