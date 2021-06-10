n=int(input())
s=[int(i) for i in input().split()]
f=[int(i) for i in input().split()]
ss=[(f[i],s[i]) for i in range(n)]
ss.sort()
# print(ss)
count=1
i=0
ff=ss[i][0]
for x in range(1,n):
    if(ss[x][1]>=ff):
        count+=1
        i=x
        ff=ss[x][0]
print(count)