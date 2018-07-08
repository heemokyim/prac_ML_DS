# *args
def asterisk_test(a, *args):
    print(type(a), a)
    print(type(args), args)

asterisk_test(1, 2, 3, 4, 5, 6)

# **kargs
def kargs_test(a, **kargs):
    print(type(a), a)
    print(type(kargs), kargs)

kargs_test(1, b=2, c=7, some='something')

# unpacking a container
asterisk_test(1, (2, 3, 4, 5, 6))

def asterisk_test2(a, args):
    print(type(a), a)
    print(type(args), *args) # unpacking

asterisk_test2(1, (2, 3, 4, 5, 6))

a, b, c = ([1, 2], [3, 4], [5, 6])
print(a, b, c)

data = ([1, 2], [3, 4], [5, 6])
print(*data) # unpacking asterisk

for d in zip(*data):
    print(d, sum(d))

def unpacking_test(a, b, c, d):
    print(a, b, c, d)

data = {'b':10, 'c':20, 'd':10000}
unpacking_test(0, **data)


