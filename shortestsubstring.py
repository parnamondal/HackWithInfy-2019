def shortest (str,n):
	disti = len(set([k for k in str]))
	return disti
def sub_distr (str):
	n = len(str)
	minl = n
	newy = shortest(str,n)
	for i in range (n):
		for j in range (n):
			stry = str[i:j]
			mo = len(stry)
			x = shortest(stry,mo)
			if ( mo < minl and x==newy ):
				minl = mo
	return minl

if __name__ == "__main__": 
	str = "AABBBCBBAE"
	l = sub_distr(str); 
	print( "The length of the smallest substring", 
		"consisting of maximum distinct", 
		"characters :", l) 


