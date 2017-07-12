import re

hand = open('mbox-short.txt')
for line in hand:
    line =line.rstrip()
    if re.search('iit',line):
        print line;
x='my 2 favourite numbers are 19 and 42'
y=re.findall('[0-9]+',x)
print y
z=re.findall('[aeiou]+',x)
print z
m='From: using the : character'
f=re.findall('^F.+:',m)
print f
#non greedy
f=re.findall('^F.+?:',m)
print f
mail='cse mail is coolvikas@cse.iitb.ac.in is my email id'
extractmail=re.findall('@([^ ]*)',mail)
print extractmail
