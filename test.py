arr1=[1,2,3,4,7,9]
arr2=[0,1,2,1,1,4]
result=[]
for ele in arr1:
	count=0
	for ele1 in arr2:
		if ele1<=ele:
			count=count+1
	result.append(count)
print(result)