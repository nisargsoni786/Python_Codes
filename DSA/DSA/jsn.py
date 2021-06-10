arr=['a','b','c','a','b','a']
d={}
for i in arr:
    d[i]=0
for i in arr:
    d[i]+=1
print(d)
f=(sorted(list(d.values())))[::-1][1]
for i in arr:
    if(d.get(i)==f):
        print(i)