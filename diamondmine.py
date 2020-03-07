from array import *
MAX=100
def dmine (arr,m,n):
	gold=[[0 for i in range (m)]for j in range (n)]
	for col in range(n-1,-1,-1):
		for row in range(m):
			if (col==n-1):
				right = 0
			else :
				right = gold[row][col+1]
			if (row==0 or col== n-1):
				right_up = 0
			else:
				right_up = gold[row-1][col+1]
			if (row==m-1 or col == n-1):
				right_down = 0
			else:
				right_down= gold[row+1][col+1]
			gold[row][col]= arr[row][col]+max(right,right_up,right_down)
	res = gold[0][0]
	for k in range(1,m):
		j=gold[k][0]
		res = max(res,j)
	return (res)
#driver code
arr =[[1,3,1,5],[2,2,4,1],[5,0,2,3],[0,6,1,2]]


 
m=4
n=4
print (dmine(arr,m,n))