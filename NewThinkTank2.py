__author__ = 'yna1'

tupleEx = ('Yusuf',17,'Gaithersburg','MD')
print tupleEx
print tupleEx[2]

tupleEx2 = (66,)
tupleEx3  =tuple("abcd")
print tupleEx3

print tupleEx3[0:2]

#list

listEx =['Yusuf',17,'Gaithersburg','MD']

print listEx[0:2]
print listEx[-1]
listNum = [1,2,3,4,5,6,7,8,9,10]
print listNum[-3:]
print listNum[:3]
print listNum[1:10:2]

print len(listNum)
print max(listNum)
print min(listNum)

listName = list('Fred')
print listName

listName[4:] = 'dy'
print listName

print ''.join(listName)#prints the list as a string

listEx2 = [1,2,3,4]
listEx2[1] = 5
print listEx2

del listEx2[1]
print listEx2

listEx.append('joy')
print listEx

listEx.remove('joy')
print listEx

listEx.remove(listEx[0])
print listEx

listEx.insert(2,'FD')
print listEx

listEx2 = ['f','e','t','g']
listEx2.sort()
print listEx2

listEx3 = [
    ['a','b','c'],
    ['d','e','f'],
    ['g','h','i'],
]

print listEx3[2][1]