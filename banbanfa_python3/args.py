import hashlib
def two(*args):
    a1,a2 = args
    print(a1,a2)
two(1,23)

def one(arg):
    a1 = arg
    print(a1)
one(1111)

md55 = hashlib.md5()

