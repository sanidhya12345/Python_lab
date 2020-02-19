t=[(), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
p=()
for i in range(0,len(t)):
   if p in t:
      t.remove(p)
print(t)
