fout = open("new.txt","w")
fout.write("hello vikas how are you?")
fout.close()
l=[]
with open("new.txt") as fin:
	for line in fin:
		l.append(line)
		print(line)


for x in l:
	m=x.split(' ')

for x in m:
	print(x)
