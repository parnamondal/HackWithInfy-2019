import sys 

def minimum_cost(a, n): 
  x=min(a)
  p=1
  s=0
  for j in range (n):
    if (a[j]!=x):
      p=x*a[j]
      s=s+p
  return s 

# Driver code 
if __name__ == "__main__": 
	
	a = [ 4, 3, 2, 5 ] 
	n = len(a) 
	print(minimum_cost(a, n)) 
