#BUBBLE SORT USING PYTHON:

lst=[20,10,5,1]
length=len(lst)-1
for count in range(length):
	for i in range(len(lst)-1):		
		if lst[i]>lst[i+1]:
			lst[i],lst[i+1]=lst[i+1],lst[i]
	length-=1
print(lst)