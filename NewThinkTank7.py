__author__ = 'yna1'

class Animal:

    __hungry = "Yes"
    __name = "No Name"
    __owner = "No Owner"

#encailation is hiding methods via 2 preceding underscores


    def __init__(self, **kvargs):
        self._attributes = kvargs


    def set_owner(self, newOwner):
        self.owner = newOwner
        return

    def get_owner(self):
        return self.owner

    def noise(self):
        print("err")
        self__hiddenMethod()
        return

    def __hiddenMethod(self):
        print "Hard to find"
    def eat(self):
        print "Crucnch, crunch"

def main():
    dog = Animal()

    dog.set_owner("Sue")
    print dog.get_owner()

    dog.noise()


main()
