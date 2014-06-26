__author__ = 'yna1'

import math

#Dictionaries

#have keys instead of indexes

dictEx = ({"Age":35,"height":"6'3","Weight":165})
#DICTIONARIES ARE Immutable

print dictEx

print dictEx.get("Age")

print dictEx.items() #Prints the keys and the values
print dictEx.values() #prints just the values

dictEx.pop("height") #removes the key and value in the parameter, which takes a key


strName ='Bob'
floatAge = 35.3
charSex ='M'
intKids = 2
boolMarried = True

print 'My name is',strName

print '%s is %.1f years old' %(strName,floatAge)

print 'Sex: %c' %(charSex)
print 'He had %d kids and said it\'s %s he is married' % (intKids,boolMarried)


print '%.15f'%(math.pi)
print '%20f' %(math.pi)
print '%20.15f' %(math.pi)
print '%-25.15f' %(math.pi)

#precisionPi = int(raw_input("How precise should pu be: "))
#print 'Pi = %.*f' %(precisionPi,math.pi)

bigString = 'Her is a loing string that i will be messing with'

print bigString[1:20:2]

print bigString.find('string')
print bigString.count("e")
print bigString.count("e",4,20)

copyStr = tuple(bigString)
print copyStr

copy2 =  ''.join(copyStr) # ''.joid(tuple) turns the tuple into a string
print copy2
copy2 =  ','.join(copyStr)
print copy2

print bigString.replace("loing","short")

print bigString.split(' ') #splits up the string into a list with each element separated by a  ' ' space
randomWhite = '                Random White Space       '
print randomWhite.strip() #this is equivalent to java trim method
