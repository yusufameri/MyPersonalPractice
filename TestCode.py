
#a place to test out code and learn and practice
'''
__author__ = 'yna1'
print __author__+ "Hello!"
print
def list_benefits():
    return ("more organized code","More readable code","Easier code reuse")

print
print list_benefits()
print

def build_sentence(info):
    return info + " is a benefit of functions"

print build_sentence("blah blah");

#this is a class called MyClass
#it has a variable and a function
print
print
print
print


#Classes------>
class MyClass:
    variable = "blah"

    def function(self):
        print "this is a message inside the class"

#this is how you make an object-->
objectx = MyClass()
#this is how you call methods on that object-->
objectx.function()
#this is how you access variables-->
print objectx.variable
#this is how you redefine that variable
objectx.variable = "not blah"
print objectx.variable






#Dictionaries------>

#this is one way to make a dictionary->
phonebook = {}
phonebook["John"] = 987654321
phonebook["Steve"] = 124537
phonebook["Bob"] = 5576354

#this is another way to make dictionaries
alternate_phonebook = {
    "John": 987654321, #dont forget to separate the values with comas
    "Steve": 124537,
    "Bob": 5576354
}

#iterating over dictionaries
    #key  #value
for name, number in phonebook.iteritems():
    print "Phone number of %s is %d" %(name, number)

#removing a value
del phonebook["John"]
#alternate way of removing a specific index
alternate_phonebook.pop("John") #returns the value of John

#sample exercise (adding jack and removing steve)
alternate_phonebook["Jack"] = 5550123
alternate_phonebook.pop("Steve") #returns the value of Steve

#generators
#->come back later
print
print
print
print
print

#List Comprehensions is a very powerful tool, which creates a new list based on another list, in a single, readable line
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()#the split function makes each word an index in a The method split() returns a list of all the words
                        # in the string, using str as the separator
                        # (splits on all whitespace if left unspecified),
print words
word_lengths = [len(word) for word in words if word != "the"]#creates a list and appends the words


user_input = raw_input("ENTER SOMETHING\n")
print "you just gave me " + user_input

if (4>2 and 3>4):
    print "yes, 4<2"
elif 2>3:
    print "this will not print"
else:
    print ("this will also not print")

example = "HELLO"
print example.isupper()
'''

'''
print 'abc', -4.24e93, 18+6.6j, 'xyz';
x, y = 1, 2;
print "Value of x , y : ", x,y;

def this_is_a_function():
    print("I am a function that is printing to the console!")


#call the function above
this_is_a_function()

#this is a function with arguments
def my_function_with_args(username, greeting):
    print "Hello, %s , From My Function!, I wish you %s"%(username, greeting)

my_function_with_args("Yusuf", "luck")

class Vehicle:
    color = ""
    price = 0.0
    type = ""

car1 = Vehicle()
car2 = Vehicle()

car1.color = "red"
car1.price = 60000
car1.type = "convertible"

def foo(first, second, third, *lal):
    print "First: %s" % first
    print "Second: %s" % second
    print "Third: %s" % third
    print "And all the rest... %s" % list(lal)

foo("yek","do","se","char","panj","shesh")

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b

print sum(number for number in xrange(1000) if not (number % 3 and number % 5))


'''
import wx

class joe(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,"The Title of the Frame",size = (300,200))

if __name__=="__main__":
    app=wx.PySimpleApp()
    frame = joe(parent=None,id=-1)
    frame.Show()
    app.MainLoop()









