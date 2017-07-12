def merge(x,y):
	l=[]
	while x and y:
		if x[0] < y[0]:
			l.append(x.pop(0))
		else:
			l.append(y.pop(0))
	for element in l:
		print(element)
	return l+x+y

x=[1,2,3,4]
y=[6,5,7,9,90]

z=merge(x,y)

for element in z:
	#pass
	print(element)