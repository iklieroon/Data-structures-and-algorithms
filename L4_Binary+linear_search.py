#Linear search

a1=[10,30,50,2,5,70,45,3]
target1=5
found1=False

for i in range (len(a1)):
    if a1[i]==target1:
        found1=True
        print(f"Element has been found at index {i}")
        break
if not found1:
    print("Element has not been found")

#The time of the above algorithm is O(n)
#Big O describes how the the run time grows as the number of elements increase and n is the number of elements

#Binary search

a2=[2,3,5,10,30,40,50,70]
target2=50
low=0
high=len(a2)-1
found2=False

while low<=high:
    mid=(low+high)//2
    if a2[mid]==target2:
        found2=True
        print(f"Element has been found at {mid}")
        break
    elif a2[mid]<target2:
        low=mid+1
    else:
        high=mid-1
if not found2:
    print("Element has not been found")