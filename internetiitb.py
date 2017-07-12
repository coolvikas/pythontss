from bs4 import BeautifulSoup
import getpass
import requests
r = requests.get('https://internet.iitb.ac.in')
#print(r.text)
flag = True
temp = ''

while flag:
	uname = input('Enter you LDAP ID: ')
	passwd = getpass.getpass('Enter your passwd ' )
	payload ={'uname':uname,'passwd':passwd}
	r = requests.post('https://internet.iitb.ac.in', data = payload)
	
	temp = r.content
	#print(temp)
	if "badpw.php" in temp:
		print("login not successful")
		continue
	elif "baned.php" in temp:
		print("No need to login u are on wireless or vpn")
		flag = False
	else:
		print("login successful")
		flag = False
soup = BeautifulSoup(temp,"html.parser")
print(soup.title)
#print(soup.get_text())
#print(soup.find_all("a"))
''' 
if "SELECT TO LOGOUT" in soup.get_text():
	print("already login")
else:
	print("no login") 

	'''