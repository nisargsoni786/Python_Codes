def rotate(a):
    a=[list(i) for i in zip(*a)]
    for i in range(len(a)):
        j=0
        k=len(a)-1
        while j<k:
            a[j][i],a[k][i]=a[k][i],a[j][i]
            j+=1
            k-=1
    return a

arr=[[1,2,3],[4,5,6],[7,8,9]]
ans=(rotate(arr))
ans=(rotate(ans))
ans=(rotate(ans))
for i in ans:
    for j in i:
        print(j,end=" ")
    print()