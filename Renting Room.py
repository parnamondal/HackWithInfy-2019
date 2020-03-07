def rent(a, arr): 
  d = a.split()
  e = arr.split()
  x=int(e[1]) *50 +int(e[2]) *100 +100
  y= int(d[1]) *50+ int(d[2]) *100
  return(x+y)
# Driver code 
a = "Standard 3 1"
arr = "Apartment 1 1"
  
print(rent(a, arr)) 
