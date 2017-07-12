#print('hello world')
def callme():
	#print(10)
	pass
for x in range(1,10,3):
	#print(x)
	#x=x+2;
	#print(x)
	callme();
x=1;
while x<10:
	#print(x)
	x += 1
my_list = [1,2,4,'hello',"me",3.145, True]

my_list.append('pypy')
#my_list.pop()
#my_list.pop(3)
#print(my_list.index(1))

for x in my_list:
	pass
	#print(x)
for index in range(0,len(my_list)):
	pass
	#print(my_list[index])

for index,value in enumerate(my_list):  # to get index value pair
	pass
	#print(index,value)

a=[1,2,3,4,5,6,7,8]
half_list=a[0:4]
for x in half_list:
	pass
	#print(x)

reverse_list=a[-1:-5:-1]
#print(a[-2])
for x in reverse_list:
	pass
	#print(x)

b=[1,2,3,4,5,6,7]
even_list=[num for num in b if num % 2 == 0]
for x in even_list:
	pass
	#print(x)

matrix = [[1,2,3],[4,5,6]]

c=['1','2','3']
str_int_list = [int(x) for x in c]
for x in str_int_list:
	pass
	#print(x)


age={}
age['george']= 10
age['mic'] = 90
print age['mic']
