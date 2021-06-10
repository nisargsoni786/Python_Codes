n=int(input())
arr=[int(i) for i in input().split()]
a=[arr[i] for i in range(n*3) if i%3==0]
sss=[arr[i] for i in range(n*3) if i%3==1]
ans=[0]*len((sss))
counter=0
b=[(arr[i+1],arr[i]) for i in range(n*3) if i%3==1]
b=sorted(b)[::-1]
sum=0
print(b)
for i in b:
    if 0 in ans[:i[1]]:
        p=i[1]-1
        while(ans[p]!=0):
            p-=1
            if p==-1:
                break
        ans[p]=i[0]
        sum+=i[0]
        counter+=1
    if counter>=len(arr):
        break
print(ans)
print(sum)
