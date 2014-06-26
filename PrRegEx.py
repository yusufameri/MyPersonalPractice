__author__ = 'yna1'

import re

f = open('text')

strToSearch  = ""

for line in f:
    strToSearch += line

print strToSearch

patFinder1 = re.compile('Aa1B') #the regex pattern goes in the parenthesis

findPat1 = re.search(patFinder1, strToSearch) #(thePatter, theStringToSearch)

print(findPat1.group())
print(findPat1.start()) #the starting index of the "Aa1B" that was found in the strToSearch
print(findPat1.end()) #the endning index of the "Aa1B" that was found in the strToSearch
print(findPat1.span()) # the "span" of the index of where "Aa1B" is located.--> (0, 4)

findPat1  = re.findall(patFinder1, strToSearch) #puts all the instances that the pattern of text was found into a list

for i in findPat1: #prints the list of the pattern that was found multiple times in the strToSearch
    print(i)

splitFound = patFinder1.split(strToSearch) #splits the documents into elements in a list. each element is separated by an instance of the pattern being found in strToSearch
print(splitFound)

subFound = patFinder1.sub('Real Text', strToSearch) #subsitutes parFinder1, which is, Aa1B, with the text, 'Real Text' in the String, strToSearch
print subFound


print
print
print
print

streetPatern = re.compile('\d{3}\s\w+\s')
thePattern = re.search(streetPatern,strToSearch)
print(thePattern.group())