import urllib
from BeautifulSoup import *

#url =raw_input('enter-')
url = "http://www.iitb.ac.in"
x= "<p>Please click <a href=http://www.dr-chuck.com>here</a></p>"
extractmail=re.findall('href=(.*)?>',x)
print extractmail
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags=soup('a')
for tag in tags:
    #print tag.get('href',None)
    pass
