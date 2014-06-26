#! /usr/bin/python
__author__ = 'yna1'


#comments

import math
#importing a single function
from math import sqrt


integerEx = 8
longIntEx = 20000000000000L
floatEx = 2.2
stringEx = "Hello"
booleanEx = True


print type(integerEx)
print type(longIntEx)
print type(floatEx)
print type(stringEx)
print type(booleanEx)

booleanTwo = False

print booleanEx and booleanTwo
print booleanEx or booleanTwo
print not booleanTwo

intOne = 7
intTwo = 99
floatOne =7.9
floatTwo = 9.8

print intTwo/intOne
print float(intTwo) / float(intOne)
print int(floatOne)

print int(booleanTwo)#returns 0 for False
print int(booleanEx)#returns 1 for True

print intOne > intTwo
print intOne >= intTwo
print intOne < intTwo
print intOne <= intTwo
print intOne == intTwo

print intOne + intTwo #plus
print intOne - intTwo #minus
print intOne * intTwo #times
print intOne / intTwo #divide
print intOne % intTwo #modulus
print intOne ** intTwo #raised to the power of

print math.sqrt(intOne)

#input

#answer = raw_input("What is your name")
#print "hello" + answer
#the comma automatically adds a space for you
#print "hello" , answer

longStr = '''THIS IS asda aweasd aaweasd
adasdawesad \
asd
'''

#the backslash prevents a new line in a multi line string
print longStr

