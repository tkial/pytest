import functools
import logging
logging.basicConfig(level=logging.INFO)
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
      

import datetime
@log
def now():
    print "12-27"
    logging.info("i am logging")

now()
print now.__name__

@log2("log2")
def now2():
    print "18:01"
now2()
print now2.__name__

#当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
int2 = functools.partial(int, base=2)
print int2("100")
print int2("100", base=10)