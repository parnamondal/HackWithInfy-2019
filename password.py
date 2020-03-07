def subarray(arrstr):
	ar=[]
	i =0
	stro =''
	ar=arrstr.split(",")
	while i < len(ar):
		arrt=[]
		s,v=ar[i].split(":") 
		p = len(s)
		arrt = [int(j) for j in str(v)]
		flag,f,m ,e= 0,0,0,0
		while m<len(arrt):
			if (arrt[m]==p) :
				flag = 1
				stro= stro+s[p-1]
				break
			m=m+1
		if (flag!=1):
			arrt.sort()
			mini=p
			while e <len(arrt):
				if (mini>=arrt[e]):
					mini = arrt[e]
					f = 1
					break
				e = e+1
			if (f==1):
				stro = stro+s[mini-1]
			else :
				stro= stro+'X'
		i =i+1
	return (stro)

if __name__ == "__main__": 
	arrstr = "Robert:65432,Tina:9528,Jo:3478"
	print (subarray(arrstr))
