def bs(arr,min,max,s):
    mid=(min+max)//2
    if arr[mid]==s:
        return (mid)
    elif arr[mid]>s:
        max=mid-1
        return bs(arr,min,max,s)
    else:
        min=mid+1
        return bs(arr, min, max, s)

arr=[-2,-1,0,1,2,3,4,5,6,7]
print(bs(arr,0,len(arr)-1,3))