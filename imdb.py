from bs4 import BeautifulSoup
import getpass
import requests
r = requests.get('http://www.imdb.com/title/tt0451279/')
temp = r.content
soup = BeautifulSoup(temp,"html.parser")

#print(soup.prettify())

rating =soup.find('span',attrs='rating-rating').contents[0]



print(soup.title)
print("rating :",rating)