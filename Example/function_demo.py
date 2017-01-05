def add_end(L=[]):
    L.append('END')
    return L

print add_end()
print add_end()
print add_end()

def add_end2(L=None):
    if L is None:
        L = []
    L.append("END")
    return L

print add_end2()
print add_end2()
print add_end2()


def calc(*args):
    print args
v = [1, 2, 3]
calc(v)
calc(*v)

def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw
person("Mike", 11)
person('Bob', 35, city='Beijing')
kw = {"company": "tencent", "job": "baba"}
person("Andy", 22, **kw)