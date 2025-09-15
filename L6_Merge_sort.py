def merge(arr,lo,mid,hi):
    new=[]
    start1=lo
    start2=mid+1
    while start1<=mid and start2<=hi:
        if arr[start1]<arr[start2]:
            new.append(arr[start1])
            start1=start1+1
        else:
            new.append(arr[start2])
            start2=start2+1
    while start1<=mid:
        new.append(arr[start1])
        start1+=1
    while start2<=hi:
        new.append(arr[start2])
        start2+1
    k=0
    for i in range(lo,hi+1):
        arr[i]=new[k]
        k+=1

def msort(arr,lo,hi):
    if lo<hi:
        mid=(lo+hi)//2
        msort(arr,lo,mid)
        msort(arr,mid+1,hi)
        merge(arr,lo,mid,hi)

arr=[1,5,3,7,8,4,7,9]
n=len(arr)
msort(arr,0,n-1)

print(arr)