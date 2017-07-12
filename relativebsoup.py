
import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
for i in range(1,9):
    #print i

    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
    l=[]
    if(i==8):
        newlist=[]
        l.append(str(soup.title))
        newlist=l[0].split(' ')[2]
        print newlist;
    tags = soup('a')
    count=0
    for tag in tags:
        count=count+1;
        if count<18:
            pass
            #print tag.get('href', None)
        else:
            #print tag.get('href', None)
            url=tag.get('href',None)
            break
