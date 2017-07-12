'''from fib import fib,fib2
fib(3)
print(fib2(4))
'''

import requests 
r = requests.get('https://internet.iitb.ac.in')
print(r.text)