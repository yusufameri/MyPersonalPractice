__author__ = 'yna1'

primesUpTo = int(raw_input("Up to what number do you want a list of prime numbers?")) - 1

list_all_numbers = []

#instantiate values in list
for i in xrange(primesUpTo):
    list_all_numbers.append(i+2)


#print the list


print
print
print
num = 2 #the actual number in the list (that is being tested and removed)
cont = True
primeList = []
oldList = list_all_numbers[:]



a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

while cont:
    for x in list_all_numbers:
        if x == num:
            a+=1
            print "a: ",a
            primeList.append(x)
            continue
        elif x % num == 0:
                c+=1
                print "c: ",c
                list_all_numbers[list_all_numbers.index(x)] = 0

    for x in list_all_numbers:
        d+=1
        print "d: ",d
        if not primeList.__contains__(x) and x != 0:
            e+=1
            print "e: ",e #GOOD
            num = x
            break
    if oldList != list_all_numbers:
        f+=1
        print "f: ",f #GOOD
        oldList = list_all_numbers[:]
        cont = True
    else:
        print "this ran" #GOOD
        cont = False

primeList = list_all_numbers[:]




for x in primeList:
    if x == 0:
        del primeList[primeList.index(x)]

print "Here is the primeList: ",primeList
print "a:%s b:%s c:%s d:%s e:%s f:%s" % (a,b,c,d,e,f)





