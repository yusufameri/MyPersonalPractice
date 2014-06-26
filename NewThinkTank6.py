__author__ = 'yna1'

def addNumbers(numOne=1,numTwo=1):
    return numOne + numTwo


ten = 10

def addNumbers(*args):
    finalValue = 0

    print ten
    if args:
        for i in args:
            finalValue += i
        return finalValue
    else:
        return "Please provide numbers"

def main():
    print addNumbers(30,2,4,634,634,457,7,5,1)


if __name__ == '__main__': main()


