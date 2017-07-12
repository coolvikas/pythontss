import re
import urllib2
data = urllib2.urlopen("http://python-data.dr-chuck.net/regex_sum_382257.txt")

numbers=[]
for line in data:

    #print line
    z=re.findall('([0-9]+)',line)
    if z:
        numbers.append(z);

x=reduce(lambda x,y:x+y,numbers)

x= [int(i)for i in x]

print sum(x)
