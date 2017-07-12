def rotate(x,y):
	if y == 0:
		return x;
	if(y>len(x)):
		return x
	length=len(x)
	#print(length)
	for element in range(0,length):
		print("element is",x[element],element)
		if element < y:
			print(x[element],element)
			z=x.pop(element)
			x.insert(element,0)
			x.append(z)
			print(x[element],element)
	for element in x:
		#pass
		print(element)
	return x[y:]

x=[1,2,3,4,5,6]
z=rotate(x,6)
print("main")
for element in z:
	print(element)