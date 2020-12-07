
"""
def abcd(func):

    def efgh(x):
        res = func(x)
        print('efgh')
        print(res)

    return efgh

def ijkl(x):
    print('ijkl')

foo = abcd(ijkl)
foo(5)

"""

def ab(x):
    def cd(y=3):
        print('cd')
    return cd

@ab
def ef():
    print('ef')

ef()