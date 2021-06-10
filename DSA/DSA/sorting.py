def selection(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr

def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def insertion(arr):
    for i in range(1,len(arr)):
        val=arr[i]
        if val > arr[i - 1]:
            continue
        if val < arr[0]:
            arr[:i + 1] = [arr[i]] + (arr[:i])
            continue
        for j in range(i-1,-1,-1):
            if(val<arr[j]):
                arr[j+1]=arr[j]
            else:
                arr[j+1]=val
    return arr

def merge(a,b):
    an,bn=0,0
    c=[]
    while an<len(a) and bn<len(b):
        if a[an]<b[bn]:
            c.append(a[an])
            an+=1
        else:
            c.append(b[bn])
            bn+=1
    if an==len(a):
        c.extend(b[bn:])
    else:
        c.extend(a[an:])
    return c

def mergesort(a):
    if len(a)==1:
        return a
    mid=len(a)//2
    return merge(mergesort(a[:mid]),mergesort(a[mid:]))

def quickextraspace(a):
    if len(a)<=1:    return a
    small,equal,large=[],[],[]
    pivot=a[0]

    for i in a:
        if i<pivot:     small.append(i)
        elif i==pivot:  equal.append(i)
        else:           large.append(i)

    return quickextraspace(small)+equal+quickextraspace(large)

def part(a,low,high):
    i=low-1
    pivot=a[high]
    for j in range(low,high):
        if(a[j]<=pivot):
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[high]=a[high],a[i+1]
    return i+1

def quicksortinplace(a,low=0,high=None):
    if high==None:
        high=len(a)-1
    if low<high:
        ind=part(a,low,high)
        quicksortinplace(a,low,ind-1)
        quicksortinplace(a,ind+1,high)
    return a

def countingsort(a,exp):
    n=len(a)
    op=[0]*n
    count=[0]*10
    for i in range(n):
        ind=a[i]//exp
        count[(ind%10)]+=1
    for i in range(1,10):
        count[i]+=count[i-1]

    i=n-1
    while i>=0:
        ind=arr[i]//exp
        count[ind%10]-=1
        op[count[ind%10]]=a[i]
        i-=1

    for i in range(n):
        a[i]=op[i]
    return a

def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp > 0:
        countingsort(arr, exp)
        exp *= 10
    return arr

def heapify(arr,n,i):
    largest=i
    l=2*i+1
    r=2*i+2

    if(l<n and arr[largest]<arr[l]):
        largest=l
    if(r<n and arr[largest]<arr[r]):
        largest=r

    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)

def heapsort(arr):
    n=len(arr)

    for i in range((n//2)-1,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)

    return arr

# arr=[5,3,4,1,2,7,6,9,8]
arr = [ 12, 11, 13, 5, 6, 7]
#print(selection(arr))
#print(bubblesort(arr))
#print(insertion(arr))
#print(mergesort(arr))
#print(quickextraspace(arr))
print(quicksortinplace(arr))
# print(radixSort(arr))
# print(countingsort(arr,1))
# print(heapsort(arr))
# print(arr)