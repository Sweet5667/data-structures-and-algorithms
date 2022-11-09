arr=[10,20,30,40,50,60,70] 
x=90
start=0
end=len(arr)-1
while end>=start:
    mid=start+(end-start)//2 
    if x==arr[mid]:
        result=mid
        break
    elif x<arr[mid]:
        end=mid-1
    else:
        start=mid+1
else:
    result=-1
if result!=-1:
    print("element is presented at index",result)
else:
    print("element not presented")
