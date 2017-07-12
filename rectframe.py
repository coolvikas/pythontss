def rect(l):
	max=0
	for element in l:
		if(len(element)>max):
			max=len(element)

	#print(max)
	for j in range(0,max+2):
				print("*",end="")
	print("")
	for element in range(0,len(l)):
		print("*",l[element],end="",sep="")
		for x in range(max-len(l[element])):
			print(" ",end="")
		print("*")
	for j in range(0,max+2):
				print("*",end="")
	print("\n")

			




l=["mira","bombaybombay","saneha","peter"]
rect(l)
