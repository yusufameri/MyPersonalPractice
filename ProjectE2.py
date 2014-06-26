__author__ = 'yna1'

def fib():
    a, b = 1, 2
    x = 1
    while a < 89:
        c = a + b
        a = b
        b = c
        yield a

        x += 1
    print a
d = fib()

g = (x for x in xrange(1000))
print sum(g)


'(Jennifer|Jen|Jenny)\b\w+\b'
'Je(nnifer|nney|n{1,6}\s\w+\s'

'(Jennifer|Jen|Jenny)\b\w+\b\1'



