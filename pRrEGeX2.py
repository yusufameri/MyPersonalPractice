__author__ = 'yna1'

import re
print "starting...\n\n\n\n\n\n\n\n\n"
f = open('text')

strToSearch = ""

for line in f:
    strToSearch += line

# print strToSearch

patFinder2 = re.compile('\d\D\s\S.\W\w',re.IGNORECASE)
findPat2 = re.findall(patFinder2, strToSearch)

for i in findPat2:
    print i

print "\n\n\n\n\n\n\n\n"





